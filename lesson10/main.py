# Set
# s1 = {1, 2, 1, 10, 2, 3}
# l1 = [1, 10, 200, 33]
# s2 = set(l1)
# print(s2)


# Добавление элементов add()

# s2.add("Hello")
# print(s2)


# Удаление элементов remove()

# item = 200
#
# if item in s2:
#     s2.remove(item)
#
# print(s2)


# clear()
# s2.clear()
# print(s2)



# Перебор множества
# for item in s2:
#     print(item)

# print(len(s2))



# Объединение множеств union()

# names = {"Erlan", "Usman", "Arman"}
# names2 = {"Bob", "Sam", "Mike"}
# union = names.union(names2)
# print(union)

# Пересечение множеств intersection()

# names = {"Erlan", "Usman", "Arman"}
# names2 = {"Bob", "Usman", "Erlan"}
# intersection = names.intersection(names2)
# print(names & names2)

# Разность множеств difference()
# names = {"Erlan", "Usman", "Arman"}
# names2 = {"Bob", "Usman", "Erlan"}
# print(names.difference(names2))

"""
Отдельная разновидность разности множеств - симметрическая разность производится с
помощью метода symmetric_difference() или с помощью операции ^.
Она возвращает все элементы обоих множеств за исключением общих
"""

# names = {"Erlan", "Usman", "Arman"}
# names2 = {"Bob", "Usman", "Erlan"}
# print(names ^ names2)


"""
Отношения между множествами
Метод issubset позволяет выяснить, является ли текущее множество подмножеством 
(то есть частью) другого множества
"""
s1 = {"Bayern", "Madrid", "Barsa"}
s2 = {"Bayern", "Madrid", "Barsa", "Chelsea", "Roma"}
# print(s1.issubset(s2)) # True


"""
Метод issuperset, наоборот, возвращает True, если текущее множество является надмножеством 
(то есть содержит) для другого множества:
"""
# print(s2.issuperset(s1)) # True

"""
Тип frozen set является видом множеств, которое не может быть изменено. 
Для его создания используется функция frozenset:
"""
s10 = frozenset({"Bayern", "Madrid", "Barsa"})
print(s10)



"""
len(s): возвращает длину множества
x in s: возвращает True, если элемент x присутствует в множестве s
x not in s: возвращает True, если элемент x отсутствует в множестве s
s.issubset(t): возвращает True, если t содержит множество s
s.issuperset(t): возвращает True, если t содержится в множестве s
s.union(t)
: возвращает объединение множеств s и t
s.intersection(t): возвращает пересечение множеств s и t
s.difference(t): возвращает разность множеств s и t
s.copy(): возвращает копию множества s
"""


