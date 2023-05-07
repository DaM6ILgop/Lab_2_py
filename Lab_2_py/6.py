import argparse
import os
import shutil
import datetime

# Парсинг аргументов командной строки
parser = argparse.ArgumentParser(description='Reorganize files in a directory.')
parser.add_argument('--source', required=True, help='Source directory path')
parser.add_argument('--days', type=int, default=0, help='Number of days to consider files as old')
parser.add_argument('--size', type=int, default=0, help='Maximum file size in bytes for the Small directory')
args = parser.parse_args()

# Получение текущей даты
current_date = datetime.datetime.now()

# Проверка и создание директории Archive
archive_dir = os.path.join(args.source, 'Archive')
if not os.path.exists(archive_dir):
    os.makedirs(archive_dir)

# Проверка и создание директории Small
small_dir = os.path.join(args.source, 'Small')
if not os.path.exists(small_dir):
    os.makedirs(small_dir)

# Перебор файлов в исходной директории
for filename in os.listdir(args.source):
    file_path = os.path.join(args.source, filename)

    # Проверка даты изменения файла
    modification_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    if (current_date - modification_date).days > args.days:
        # Перемещение файла в директорию Archive
        shutil.move(file_path, os.path.join(archive_dir, filename))

    # Проверка размера файла
    if os.path.getsize(file_path) < args.size:
        # Перемещение файла в директорию Small
        shutil.move(file_path, os.path.join(small_dir, filename))