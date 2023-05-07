import os
import hashlib

# Функция для вычисления контрольной суммы файла
def get_md5(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        md5 = hashlib.md5(data).hexdigest()
    return md5

# Функция для поиска дубликатов файлов
def find_duplicate_files(directory):
    # Словарь, где ключом является контрольная сумма файла, а значением - список файлов с такой же контрольной суммой
    files_by_md5 = {}

    # Проходимся по всем файлам в директории и ее подпапках
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            # Полный путь к файлу
            file_path = os.path.join(root, file_name)
            # Вычисляем контрольную сумму файла
            file_md5 = get_md5(file_path)
            # Добавляем файл в соответствующий список в словаре
            if file_md5 in files_by_md5:
                files_by_md5[file_md5].append(file_path)
            else:
                files_by_md5[file_md5] = [file_path]

    # Фильтруем словарь, оставляя только списки файлов с более чем одним элементом (т.е. дубликаты)
    duplicate_files = {md5: files for md5, files in files_by_md5.items() if len(files) > 1}

    # Выводим группы дубликатов
    for md5, files in duplicate_files.items():
        print('Дубликаты с контрольной суммой', md5)
        for file in files:
            print(file)
        print()

# Пример использования
find_duplicate_files('labtest')