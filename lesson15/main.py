# # # try:
# # #     print(int("hello"))
# # #     print(10 / 0)
# # # except ZeroDivisionError:
# # #     print("zero error")
# # # except ValueError:
# # #     print("Ошибка с Value error")
# #
# # number = int(input("Insert number: "))
# # if number > 5:
# #     raise Exception("Число больше 5")
# # else:
# #     print("good good")
#
#
# class PersonAgeException(Exception):
#     def __init__(self, age, minage, maxage) :
#         self.age = age
#         self.minage = minage
#         self.maxage = maxage
#
#     def __str__(self) :
#         return f"Недопустимое значение: {self.age}. " \
#                f"Возраст должен быть в диапазоне от {self.minage} до {self.maxage}"
#
#
# class Person :
#     def __init__(self, name, age) :
#         self.__name = name  # устанавливаем имя
#         minage, maxage = 1, 110
#         if minage < age < maxage :  # устанавливаем возраст, если передано корректное значение
#             self.__age = age
#         else :  # иначе генерируем исключение
#             raise PersonAgeException(age, minage, maxage)
#
#     def display_info(self) :
#         print(f"Имя: {self.__name}  Возраст: {self.__age}")
#
#
# try :
#     tom = Person("Tom", 37)
#     tom.display_info()  # Имя: Tom  Возраст: 37
#
#     bob = Person("Bob", -23)
#     bob.display_info()
# except PersonAgeException as e :
#     print(e)  # Недопустимое значение: -23. Возраст должен быть в диапазоне от 1 до 110
from functools import reduce

