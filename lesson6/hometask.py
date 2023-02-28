"""
1. calculate_exponent(5, 5) ➞ 3125
 calculate_exponent(10, 10) ➞ 10000000000
 calculate_exponent(3, 3) ➞ 27
В данной задаче должны получить результат из двух чисел, результат умножения.
2. how_many_times(5) ➞ "Edaaaaabit"
 how_many_times(0) ➞ "Edbit"
 how_many_times(12) ➞ "Edaaaaaaaaaaaabit"
В данной задаче мы должны букву "а" произвести столько раз, сколько у нас имеется число заданное нами
3. Create a function which returns the length of a string, without using len().Examples length("Hello World") ➞ 11
length("Edabit") ➞ 6
length("wash your hands!") ➞ 16
В данной задаче, мы должны определить количество букв, без функции len()
4. Даны целые числа A и B (A < B).
Вывести все целые числа от A до B включительно; при этом число A должно выводиться 1 раз, число A + 1 должно выводиться 2 раза и т. д.
5. Дано целое число, к примеру 1278493.
Необходимо определить есть ли число 7 в искомом числе.
"""

# task 1
# number1 = int(input("Insert num1: "))
# number2 = int(input("Insert num2: "))
# result = 1
# for i in range(1, number2 + 1):
#     result *= number1
#
# print(result)

# task 2
# message = "Edbit"
# text = ""
# number1 = int(input("Insert num1: "))
# for i in range(number1):
#     if number1 < 0 or number1 == 0:
#         print(message)
#         break
#     text += "a"
# print("Ed" + text + message[2::])


# task 3
# count = 0
# message = "almaty"
# for i in message:
#     count += 1
# print(count)

# task 4
# number1 = int(input("Insert num1: "))
# number2 = int(input("Insert num2: "))
# count = number1
# for i in range(number1, number2 + 1):
#     for j in range(i):
#         print(count, end=" ")
#         count += 1
#     print()

# task 5
# number1 = int(input("Insert num1: "))
# text = str(number1)
# print(str(7) in text)


