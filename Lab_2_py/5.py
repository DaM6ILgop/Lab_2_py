import re

# Ввод текста с клавиатуры
text = input("Введите текст: ")

# Поиск слов, соответствующих условию
pattern = r'\b[A-Z][a-zA-Z]*\d{2}(?:\d{2})?\b'
matches = re.findall(pattern, text)

# Вывод найденных слов
for match in matches:
    print(match)