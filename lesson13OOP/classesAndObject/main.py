# # OOP
# class Human:
#
#     # constructor(метод который сработает при инициализации объекта)
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # action (действия)
#     def move(self):
#         return f"{self.name} is moving, age: {self.age}"
#
#     def __str__(self):
#         return f"{self.name}, {self.age}"
#
# h1 = Human("Erlan", 29)
# print(h1.move())


# Task

class Student:
    def __init__(self, id, name, surname, gpa):
        self.id = id
        self.name = name
        self.surname = surname
        self.gpa = gpa

    def getStudentData(self):
        return f"{self.id}, {self.name}, {self.surname}, {self.gpa}"

    def __str__(self):
        return f"{self.id}, {self.name}, {self.surname}, {self.gpa}"


allStudent = [Student(1, "Erlan", "Karabaliyev", 3.5), Student(2, "Arman", "Nurbergen", 3.4), Student(3, "Usman", "ErlanUly", 3.7)]
# b = list(filter(lambda student: student.gpa > 3.4, allStudent))
# c = list(map(lambda st: st.gpa + 1, allStudent))
#
# print(c)

# task 1 Hometask
# def topStudent(students):
#     return max(students, key=lambda x: x.gpa)
#
# print(topStudent(allStudent))

# task 2

# while True:
#     print("[1] add student")
#     print("[2] list student")
#     print("[0] exit")
#     choice = int(input("Insert choice: "))
#     if choice == 1:
#         id = int(input("Insert id: "))
#         name = input("Insert name: ")
#         surname = input("Insert surname: ")
#         gpa = float(input("Insert gpa: "))
#         allStudent.append(Student(id, name, surname, gpa))
#     elif choice == 2:
#         for st in allStudent:
#             print(st.getStudentData())
#     elif choice == 0:
#         break


# task 3

class Player:
    def __init__(self, number, name, surname, position):
        self.number = number
        self.name = name
        self.surname = surname
        self.position = position


    def toString(self):
        return f"{self.number}, {self.surname}, {self.name}"


class Club:
    def __init__(self, name, country, rating, players):
        self.name = name
        self.country = country
        self.rating = rating
        self.players = players

    def printClubData(self):
        print(f"{self.name}, {self.country}, {self.rating}")
        print("Players ")
        for pl in self.players:
            print(pl.toString())

players = [Player(1, "Manuel", "Neuer", "keeper"), Player(10, "Sergeu", "Gnabry", "forward")]
club1 = Club("Bayern", "Germany", 10, players)
club1.printClubData()