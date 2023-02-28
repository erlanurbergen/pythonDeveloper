# from functools import reduce
from PIL import Image
# # Bonus
# # enumerate()
# # lambda(анонимные функции)
# # list comprehension(генератор списков)
# # двумерные массивы(вложенными списками)
# # Функции map(), filter(), reduce(), zip()
# # *args, **kwargs
#
# # l1 = [10, 20, 1, 5, -8, 17]
# # # l1 = ("Hello", 7, 0, 8)
# # set1 = {10, 19, 29, 5}
# # dict1 = {1 : "Hello", "age": 29}
# # # b1 = list(enumerate(l1))
# # # print(b1)
# #
# # for index, value in enumerate(l1):
# #     l1[index] = value + 1
# #
# # print(l1)
#
#
# # lambda(анонимные функции)
#
# # def getSize(a):
# #     return len(a)
#
#
# # def getSum(a, b, c):
# #     return a + b + c
# #
# # text = "Hello"
# # func = lambda x: len(x)
# # sum1 = lambda a, b, c: a + b + c
# # print(sum1(10, 10, 10))
#
# # num = int(input("Insert num: "))
#
# # def getPosAndNeg(num):
# #     if num > 0 :
# #         return "positive"
# #     return "negative"
#
# # getPosAndNeg = lambda x: "pos" if x > 0 else "negative"
# #
# # print(getPosAndNeg(num))
#
# # l1 = [10, 117, 42, -9, 8, 1033, 321, 99]
# # l1.sort(key = lambda x: x % 10)
# # print(l1)
#
# # [выражение for value in коллекция if выражение]
# # b = [10, 20, 1, 9, 7]
# # a = [i for i in b if i > 7 and i % 2 != 0]
# # c = [ord(i) for i in "hello"]
# # x = [i for i in range(5) for j in range(10) if i + j >= 10]
# # array2 = [[i] * 5 for i in range(5)]
#
#
# # for i in array2: # i = []
# #     for j in i:
# #         print(j, end=" ")
# #     print()
#
# # for i in range(len(array2)):
# #     for j in range(len(array2[i])):
# #         if i == j:
# #             array2[i][j] = 0
# #         elif i < j:
# #             array2[i][j] = 1
# #         else:
# #             array2[i][j] = 2
#
# # for i in array2: # i = []
# #     for j in i:
# #         print(j, end=" ")
# #     print()
#
# # map() - (func, *iterable) -> map object
#
# # a = [10, -9, 11, -3, -4]
# # l1 = [[1, 4, 3], [1, 2, 6], [1, 2, 3]]
# # b = list(map(max, l1))
# # print(b)
#
# # texts = ["hello", "hi", "sir"]
# # text = "yetyrtywh676hdg7h87"
# # # b = list(map(lambda x: x*2, a))
# #
# # b = list(map(str.isalpha, text))
# # print(b)
# # filter() - (func or None, *iterable) -> filter object
#
# # a = [10, -9, 11, -3, -4]
# # c = ["Hello", "How are you", "Good day"]
# # b = list(filter(lambda x: len(x) > 5, c))
# # print(b)
#
# # reduce()
#
# # a = [10, -9, 11, -3, -4]
# # b = reduce(lambda x, y: x * y, a)
# # print(b)
#
# # zip()
# # a = [1, 2, 3, 4] # 4
# # b = [10, 20, 30] # 3
# #
# # for i, b in zip(a, b):
# #     print(i, b)
#
# # args
#
# a = [1, 2, 3, 4]
# print(*a)
#
# def getSum(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
#
# def printHello(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
#
# printHello(a=10, b=20, c=99)
#
