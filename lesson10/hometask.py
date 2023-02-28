"""
1. На входе функция to_set() получает строку или список чисел.
Преобразуйте их в множество. На выходе должно получиться множество и его мощность.

2. Напишите функцию superset(), которая принимает 2 множества.
Результат работы функции: вывод в консоль одного из сообщений в зависимости от ситуации:
1 - «Супермножество не обнаружено»
2 – «Объект {X} является чистым супермножеством»
3 – «Множества равны». Подсказка (if set_1 > set_2:
print(f'Объект {set_1} является чистым супермножеством'))

3. Напишите программу, которая определяет количество различных символов, встречающихся в символьной строке.
входные данные aB12A
выходные данные 5

4. Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
"""

# task 1
# def to_set(a):
#     return set(a)
#
# print(to_set("hello"))

# task 2

# def superset(set_1, set_2):
#     if set_1 > set_2:
#         print(f'Объект {set_1} является чистым супермножеством')
#     elif set_1 == set_2:
#         print(f'Множества равны')
#     elif set_1 < set_2:
#         print(f'Объект {set_2} является чистым супермножеством')
#     else:
#         print('Супермножество не обнаружено')
#
# superset({1, 2, 3, 4}, {1, 2, 3})

# task 3

# def differnce(a):
#     return len(set(a))
#
# print(differnce("aB122AB"))

# task 4

def getRes(a, b):
    set1 = set(a)
    set2 = set(b)
    return set1.difference(set2)

print(getRes([1, 2, 3], [4, 1, 6]))

