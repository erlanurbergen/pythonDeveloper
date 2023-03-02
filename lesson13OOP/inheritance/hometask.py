import random
"""
1. Создайте класс User с параметрами:
int id
String login
String password
String name
String surname
Геттеры и сеттеры
+String getData() // Данный метод возвращает все данные пользователя

Создайте 2 класса которые наследуют от класса User:
1 – Staff
+double salary
+String subjects[]
Геттеры и сеттеры
Переопределите метод getData(), относительно их параметрам

2 – Student
+double gpa
+String coruses[]
Геттеры и сеттеры
Переопределите метод getData(), относительно их параметрам
Вы должны создать как минимум по 5 объектов класса Student, Staff и Users, и добавить их в массив из класса Users.

2. Создайте меню для первого задания, где вы управляете студентами, рабочими и пользователями.
PRESS [1] ADD USER

   PRESS [1] TO ADD STUDENT

   PRESS [2] TO ADD STAFF

PRESS [2] TO LIST USERS

   PRESS [1] TO LIST STUDENTS

   PRESS [2] TO LIST STAFF

PRESS [0] TO EXIT

(Подсказка: Фильтр вывода студента или рабочего нужно реализовать с помощью ключевого

слова: isinstance)

instanceof - специальное ключевое слово, которая возвращает true, если объект является типом

данного класса.
"""

class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def getData(self):
        return f"{self.login}, {self.password}"


class Staff(User):

    def __init__(self, login, password, salary, subjects) :
        super().__init__(login, password)
        self.salary = salary
        self.subjects = subjects

    def getData(self) :
        return super().getData() + f"{self.salary}, {self.subjects}"

class Student(User):

    def __init__(self, login, password, gpa, subjects):
        super().__init__(login, password)
        self.gpa = gpa
        self.subjects = subjects

    def getData(self) :
        return super().getData() + f"{self.gpa}, {self.subjects} "


users = [User("user", "123"),
         Staff("staff", "111", 500000, ["math", "history"]),
         Student("student", "444", 3, ["c++", "python"])
         ]

studentLogin = ["std1", "std2", "std3", "std4"]
studentPassword = ["std1", "std2", "std3", "std4"]
StudentsGpas = [1, 2, 3, 4]
studentsSubjects = [["c++", "java"], ["python", "golang"], ["php", "c#"]]

# for user in users:
#     print(user.getData())
while True:
    print("""
    PRESS [1] ADD USER
    PRESS [2] TO LIST USER
    PRESS [0] TO EXIT
    """)
    choice = int(input("Insert choice: "))
    if choice == 1:
        print("""
        PRESS [1] TO ADD STUDENT
        PRESS [2] TO ADD STAFF
        """)
        choice2 = int(input("Insert choice: "))
        if choice2 == 1:
            users.append(Student(random.choice(studentLogin), random.choice(studentPassword), random.choice(StudentsGpas), random.choice(studentsSubjects)))
    elif choice == 2:
        print("""
                PRESS [1] TO List STUDENT
                PRESS [2] TO List STAFF
                """)
        choice2 = int(input("Insert choice: "))
        if choice2 == 1:
            print(users[len(users) - 1].getData())
