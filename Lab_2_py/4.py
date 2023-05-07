import re

# Ввод имени текстового файла
filename = input("Введите имя текстового файла: ")

# Чтение файла
with open(filename, 'r') as file:
    text = file.read()

# Поиск подстрок с помощью регулярных выражений
pattern = r'[A-Z]:\\(?:[^\/:?"<>|\r\n]+\\)+[^\/:*?"<>|\r\n]+'
matches = re.findall(pattern, text)

# Вывод найденных подстрок
for match in matches:
    print(match)