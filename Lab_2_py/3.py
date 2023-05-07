import os

# Задаем путь к директории с музыкальными файлами
path = 'music'

# Открываем текстовый файл со списком песен
with open('music\\music-info.txt', 'r') as f:
    # Читаем все строки файла
    lines = f.readlines()

# Проходимся по каждой строке списка песен
for line in lines:
    # Извлекаем номер и название песни
    number, title = line.strip().split('. ', 1)

    # Форматируем номер песни, чтобы было две цифры (например, '01')
    number = number.zfill(2)

    # Формируем новое имя файла на основе номера и названия песни
    new_name = f'{number} - {title}.mp3'

    # Получаем полный путь к файлу в директории
    old_path = os.path.join(path, title + '.mp3')
    new_path = os.path.join(path, new_name)

    # Переименовываем файл, если он существует
    if os.path.exists(old_path):
        os.rename(old_path, os.path.join(path, new_name))