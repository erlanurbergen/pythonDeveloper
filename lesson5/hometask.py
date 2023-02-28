import math
"""
1. Дано трехзначное число. Проверить истинность высказывания:
«Цифры данного числа образуют возрастающую последовательность»
2. Даны целые числа a, b, c. Проверить истинность высказывания:
«Существует треугольник со сторонами a, b, c»
3. Дано целое число. Вывести его строку-описание вида «отрицательное четное число»,
 «нулевое число», «положительное нечетное число» и т. д.
"""

# task 1
# x = int(input("Insert x: ")) # 123 -> 321
# firstNumber = math.trunc(x / 100)
# secondNumber = math.trunc(x / 10) % 10
# thirdNumber = x % 10
#
# # if firstNumber < secondNumber and secondNumber < thirdNumber:
# #     print("Yes")
# # else:
# #     print("no")
#
# print(firstNumber < secondNumber < thirdNumber if "yes" else "no")

# task 2
# m = int(input("Insert m: "))
# n = int(input("Insert n: "))
# u = int(input("Insert u: "))
# if m + n >= u:
#     if n + u >= m:
#         if m + u >= n:
#             print("Yes")
#         else:
#             print("No")

# task 3

m = int(input("Insert m: "))
if m != 0:
    print("Не нулеове число")
    if m > 0 and m % 2 == 0:
        print("Positive and even number")
    else:
        print("Negative and odd number")
