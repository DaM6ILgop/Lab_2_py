import string
import unicodedata

# Открываем файл и читаем его
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Инициализируем словарь для отслеживания количества символов
char_count = {}

# Проходимся по каждому символу в тексте
for char in text:
    # Пропускаем символы, которые не являются буквами
    if not unicodedata.category(char).startswith('L'):
        continue

    # Приводим символ к нижнему регистру
    char = char.lower()

    # Если символ уже есть в словаре, увеличиваем его количество на 1
    if char in char_count:
        char_count[char] += 1
    # Иначе добавляем символ в словарь с начальным значением 1
    else:
        char_count[char] = 1

# Сортируем словарь по значению в порядке убывания
sorted_chars = sorted(char_count, key=char_count.get, reverse=True)

# Выводим символы в порядке убывания частоты встречаемости
for char in sorted_chars:
    print(char, char_count[char])