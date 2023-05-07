import argparse
import os
import random
from pydub import AudioSegment

# Парсинг аргументов командной строки
parser = argparse.ArgumentParser(description='Create a track mix from short fragments of MP3 files.')
parser.add_argument('--source', '-s', required=True, help='Source directory path')
parser.add_argument('--destination', '-d', help='Destination file name')
parser.add_argument('--count', '-c', type=int, help='Number of files in the mix')
parser.add_argument('--frame', '-f', type=int, help='Number of seconds per file')
parser.add_argument('--log', '-l', action='store_true', help='Enable logging')
parser.add_argument('--extended', '-e', action='store_true', help='Apply fade in/fade out to each fragment')
args = parser.parse_args()

# Определение пути к директории исходных файлов и пути к выходному файлу
source_dir = args.source
destination_file = args.destination or os.path.join(source_dir, 'mix.mp3')

# Получение списка файлов в директории
files = [f for f in os.listdir(source_dir) if f.endswith('.mp3')]

# Определение количества файлов для обработки
file_count = args.count if args.count and args.count <= len(files) else len(files)

# Определение продолжительности фрагмента
frame_duration = args.frame or 10

# Инициализация списка для хранения информации о фрагментах
fragments = []

# Перебор случайно выбранных файлов и создание фрагментов
for i in range(file_count):
    # Выбор случайного файла
    file = random.choice(files)

    # Удаление выбранного файла из списка для предотвращения повторной обработки
    files.remove(file)

    # Определение пути к выбранному файлу
    file_path = os.path.join(source_dir, file)

    # Загрузка аудиофайла с помощью pydub
    audio = AudioSegment.from_file(file_path, format='mp3')

    # Определение продолжительности файла
    file_duration = len(audio) / 1000

    # Расчет начальной точки для обрезки файла
    start_time = random.uniform(0, file_duration - frame_duration)

    # Обрезка аудиофайла для создания фрагмента
    fragment = audio[int(start_time * 1000):int((start_time + frame_duration) * 1000)]

    # Добавление фрагмента в список
    fragments.append(fragment)

    # Создание папки для сохранения фрагментов, если она не существует
    os.makedirs(os.path.join(source_dir, 'fragments'), exist_ok=True)
    
    # Сохранение фрагмента
    fragment_file = os.path.join(source_dir, 'fragments', f'fragment_{i}.mp3')
    fragment.export(fragment_file, format='mp3')

# Объединение фрагментов в обзорный трек-микс
mix = AudioSegment.silent(duration=0)
for fragment in fragments:
    mix += fragment

# Применение эффекта fade in/fade out, если указан флаг --extended
if args.extended:
    fade_duration = 1000  # Длительность эффекта fade in/fade out в миллисекундах
    mix = mix.fade_in(fade_duration).fade_out(fade_duration)

# Сохранение обзорного трек-микса
mix.export(destination_file, format='mp3')

# Вывод лога процесса обработки файлов, если указан флаг --log
if args.log:
    print('--- processing files ---')
    for i, file in enumerate(files):
        print(f'processing file {i+1}: {file}')
    print('--- done! ---')
    print(f'Total fragments created: {len(fragments)}')