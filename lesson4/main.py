# String(Строки)str

"""
Конкатенация (сложение)
Дублирование строки
Длина строки (функция len)
Доступ по индексу
Извлечение среза
isalpha()
islower()
isupper()
isdigit()
isnumeric()
startswith(str)
endswith(str)
lower()
upper()
title()
capitalize(): переводит в верхний регистр первую букву только самого первого слова строки
lstrip(): удаляет начальные пробелы из строки
rstrip(): удаляет конечные пробелы из строки
strip(): удаляет начальные и конечные пробелы из строки
find(str[, start [, end]): возвращает индекс подстроки в строке. Если подстрока не найдена, возвращается число -1
replace(old, new[, num]): заменяет в строке одну подстроку на другую
split([delimeter[, num]]): разбивает строку на подстроки в зависимости от разделителя
join(strs): объединяет строки в одну строку, вставляя между ними определенный разделитель
"""

# Конкатенация (сложение)
# str1 = "Hello"
# str2 = "World"
# print(str1 + str2)

# Сравнение строк
# print(str1 > str2) # по первой букве вхождения 72 > 87

# Дублирование строки
# print("Hello" * 3)

# Длина строки (функция len)
# print(len("Hello"))

# Доступ по индексу
# str1 = "Hello"
# print(str1[-5])

# Извлечение среза
# str1 = "Hello world"
# # print(str1[::-1]) # reverse
# print(str1[-6::-1])

# isalpha()
# str1 = "Helloworld"
# print(str1.isalpha())

# isdigit()
# str1 = "7676766"
# print(str1.isdigit())

#islower()
# isupper()

# str1 = "hello"
# print(str1.islower()) # True
# print(str1.isupper()) # False

# startswith(str)
# str1 = "hello"
# print(str1.startswith("he"))

# endswith(str)
# str1 = "hello"
# print(str1.endswith("7lo"))

#lower()
# upper()
# title()
# str1 = "hello"
# title = str1.title()
# print(title)

# capitalize()
# print("hello world".capitalize())

# lstrip()
# str1 = " hello"
# print(str1.lstrip())

# rstrip()
# str1 = "hello "
# print(str1.rstrip())

#strip()
# str1 = " hello "
# print(str1.strip())

# find(str[, start [, end]):
# str1 = "hello world world"
# print(str1.find("wo", 11))

# replace(old, new[, num])
# number = "+7-708-765-88-10"
# print(number.replace("-", " "))

# split
# data = "Hello Sam how are you?"
# split = data.split(" ") # list
# print(split)

# join()
# list = ["User", "Admin", "Manager"]
# data = " ".join(list)
# print(data)




