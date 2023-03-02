import random
# Dictionaty
# Как создать словарь

data = {"name": "Erlan", "age": 29, "hobbies": ["football", "basketball"]}
# print(data)
# Как получить элементы из словаря
# print(data["hobbies"][0])
# print(data.get("hobbies")[0])

# for i in data.keys():
#     print(i, data[i])

def helloHello():
    print("hello")
# Как изменить или добавить элементы в словаре
data["age"] = 30
data["city"] = "Almaty"

# for i in enumerate(data):
#     print(i)
# print(data)


# Как удалить элементы из словаря
"""
Удалить нужный элемент словаря по ключу можно с помощью метода pop().
Этот метод удаляет элемент с соответствующим ключом и возвращает значение.
"""
# del data["age"]
# data.pop("age")
# print(data)


# Превратить List в Dict

# res = [["name", "Erlan"], ["city", "Almaty"]]
# data2 = dict(res)
# print(data2)

# fromkeys()

items1 = {}.fromkeys(["banana", "apple", "orange"], random.randint(1, 4))
print(items1)

# update()
# data.update(items1)
# items1.update(data)
# print(items1)


# values()

print(data.values())

# keys()

print(data.keys())









