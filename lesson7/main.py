# Функции def
# Параметры функции
# Оператор return и возвращение результата из функции

# def hello(name, age = 10):
#     print("hello {}, age {}".format(name, age))
#
#
# hello("Erlan")
# hello("Arman", 9)
# hello("Usman", 9)

def getData(name, age):
    return f"name: {name}, age: {age}"


userData = getData("Erlan", 29)
print(type(userData))
