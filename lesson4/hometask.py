import random
"""
1.Дан символ C. Вывести его код (то есть номер в кодовой таблице)
2. Дано целое число N (32 < N < 126). Вывести символ с кодом, равным N
3. Дана строка. Вывести строку, содержащую те же символы, но расположенные в обратном порядке
4. Дана строка. Подсчитать количество содержащихся в ней цифр
5. Дана строка. Подсчитать количество содержащихся в ней прописных
латинских букв
6. Даны строки S и S0. Проверить, содержится ли строка S0 в строке S.
Если содержится, то вывести TRUE, если не содержится, то вывести FALSE.
7. Определить является ли строка полиндромом
"""

# task 1
# c = 'W'
# print(ord(c))

# task 2
# n = random.randint(32, 126)
# print(n, "->", chr(n))

# task 3
# message = "Hello"
# print(message[::-1])

# task 4
# message = "Hello 2023 year!!!!!"
# count = 0
# for i in message:
#     if i.isdigit():
#         count += 1
# print(count)

# task 5

# message = "Hello 2023 year!!!!!"
# count = 0
# for i in message:
#     if i.isalpha():
#         count += 1
# print(count)

# task 6
# s = "hello"
# s0 = "ll"
# print(s0 in s)

# task 7
# message = "oppo2"
# print(message == message[::-1])
#



