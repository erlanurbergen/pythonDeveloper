import random
# list - списки
# l1 = list(range(1, 10, 2))
# print(l1)
#
# l2 = [1, 2, 3, 4]
# print(l2)

# l3 = ["Hello", True, 3.4, 100, [1, 2, 3], {1, 2, 3}]
# print(random.choice(l3))
# print(l3[-1])
# print(l3[3])
# for i in l3:
#     print(type(i))
#
# print(l3)
#
# for i in l3:
#     print(i)

# for i in range(len(l3)):
#     if l3[i] == 3.4:
#         print(i, l3[i])


# Разложение списка
# append(item): добавляет элемент item в конец списка
# insert(index, item): добавляет элемент item в список по индексу index
# extend(items): добавляет набор элементов items в конец списка
# remove(item): удаляет элемент item. Удаляется только первое вхождение элемента.
# Если элемент не найден, генерирует исключение ValueError
# clear(): удаление всех элементов из списка
# index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError
# pop([index]): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.
# count(item): возвращает количество вхождений элемента item в список
# sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.
# reverse(): расставляет все элементы в списке в обратном порядке
# sorted(list, [key]): возвращает отсортированный список
# min(list): возвращает наименьший элемент списка
# max(list): возвращает наибольший элемент списка


# l3 = ["Hello", True, 3.4, 100, [1, 2, 3], {1, 2, 3}]
# append(item)
# l3 = ["Hello", True, 3.4, 100, [1, 2, 3], {1, 2, 3}]
# l3.append(2000)
# print(l3)

# insert(index, item)
# l3.insert(0, 3400)
# print(l3)


# extend(items)
# l2 = [1, 2, 3, 9]
# l3.extend(l2)
# print(l3)

# remove(item)
# l3.remove(3.4)
# print(l3)

# clear():
# l3.clear()
# print(l3)

# index(item)
# print(l3.index(True))

# pop([index])
# l3.pop()
# print(l3)

# count(item)
# print(l3.count(True))


l3 = [100, 4, 3, -9, 10]

# sort([key])
# l3.sort(reverse=True)
# print(l3)

# sorted(list, [key]):
# l4 = sorted(l3, reverse=True)
# print(l4)

# min, max

# print(max(l3))
# print(min(l3))
