"""
Задача 1.
Программа принимает число x - длину словаря. После чего с консоли будут
введены x строк, состоящий строго из двух слов. Ваша задача создать
словарь, записать ключ и значение. Ключом будет первое слово каждой
строки, вторым слово - значение.
Hint: использовать цикл для введения с консоли
Пример:
input:
3 # длина словаря
name Python # name - key, Python - value
address Almaty # address - key, Almaty - value, и т.д.
room empty
output:
{“name”: “Python”, “address”: ”Almaty”, “room”: “empty”}
"""
#
# size = int(input("Insert size: "))
# data = dict()
# for i in range(size):
#     text = input("Insert text: ").split()
#     data[text[0]] = text[1]
#
# print(data)


"""
Программа принимает число x. Создать словарь, состоящий из ключей и
значений. Ключами являются числа от 0 до x, а значением является куб этого
числа.
Пример:
input:
5
output:
{0: 0, 1:1, 2:8, 3:27, 4:64, 5:125}
input:
2
output:
{0:0, 1:1, 2:8}
"""

# x = int(input("Insert x: "))
# # 1 option
# # dict = {i:i**3 for i in range(x+1)}
#
# data = dict()
# for i in range(x+1):
#     data[i] = i ** 3
# print(data)


"""
Модифицировать код задачи №2 так, что вы используете dictionary
comprehension. Input и output совпадают со второй задачей.
"""

# x = int(input("Insert x: "))
# dict = {i:i**3 for i in range(x+1)}
#
# print(dict)
"""
У вас есть словарь employee (не надо делать инпут). В словаре employee
поменяйте зарплату сотрудника John на 300000.

"""

# employees = {
#     'employee1' : {'name': 'Sam', 'age': 35, 'salary': 400000},
#     'employee2' : {'name': 'Anna', 'age': 29, 'salary': 350000},
#     'employee3' : {'name': 'John', 'age': 25, 'salary': 250000},
# }
# employees['employee3']['salary'] = 300000
# print(employees)


"""
У вас есть словарь employee (не надо делать инпут). В словаре employee
удалите employee3.
employees = {
    'employee1' : {'name': 'Sam', 'age': 35, 'salary': 400000},
    'employee2' : {'name': 'Anna', 'age': 29, 'salary': 350000},
    'employee3' : {'name': 'John', 'age': 25, 'salary': 250000},
}
"""
# employees = {
# #     'employee1' : {'name': 'Sam', 'age': 35, 'salary': 400000},
# #     'employee2' : {'name': 'Anna', 'age': 29, 'salary': 350000},
# #     'employee3' : {'name': 'John', 'age': 25, 'salary': 250000},
# # }
# # del employees['employee3']
# # print(employees)


"""
Программа принимает строку. Ваша задача создать словарь. Этот словарь
будет хранить ключи “digits” и “alphas”. Ваша задача определить сколько
букв и цифр есть в введенной строке. Записать количество букв как значение
“alphas”, а цифр в “digits”.
Hint: ASCII code maybe?

"""

def res(text):
    data = dict()
    digit = 0
    alpha = 0
    for item in text:
        if item.isdigit():
            digit += 1
            data["digit"] = digit
        elif item.isalpha():
            alpha += 1
            data["alpha"] = alpha
    return data

print(res("hello123"))

