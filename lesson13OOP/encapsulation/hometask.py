"""
1. Создайте класс User с параметрами:
- int id;
- String login;
- String password;
- String role;
+ String toString() // Данный метод возвращает все данные пользователя. Но, для возврата, используйте геттеры и сеттеры а не поля.
Геттеры и сеттеры для каждого параметра.
Cоздайте несколько объектов класса Users и добавьте их в массив. Далее, используя цикл, выведите логин каждого пользователя.


2. Во втором задании, вы должны заранее в массив добавить 10 объектов класса Users.
Используйте данный массив как базу данных пользователей.
При запуске программы, у вас должны запрашивать логин и пароль
INSERT LOGIN:
     Вводите логин
INSERT PASSWORD:
     Вводите пароль
При верном раскладе, программа должна вас запустить
Welcome Erlan
PRESS [1] TO EDIT LOGIN
      Insert login
PRESS [2] TO CHANGE PASSWORD
      Insert old password
      Insert new password
      Re-Insert new password
PRESS [3] TO DELETE OWN ACCOUNT
PRESS [0] TO EXIT
"""


# task 1
class User:
    def __init__(self, id, login, password, role):
        self.__id = id
        self.__login = login
        self.__password = password
        self.__role = role


    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login) :
        self.__login = login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        passw = hash(self.__password)
        return f"{self.__id}, {self.__login}, {passw}"


users = [User(1, "admin", "123", "admin"), User(2, "user", "333", "guest")]
print(users[0])

login = input("Insert login: ")
password = input("Insert password: ")
for user in users:
    if user.password == password and user.login == login:
        print(f"welcome {user.login}")
        while True :
            print("PRESS [1] TO EDIT LOGIN")
            print("PRESS [2] TO CHANGE PASSWORD")
            print("PRESS [3] TO DELETE OWN ACCOUNT")
            print("PRESS [0] EXIT")
            choice = int(input("Insert choice: "))
            if choice == 1:
                login = input("Insert new login: ")
                user.login = login
                print(user.login)
            elif choice == 2:
                password = input("Insert new password: ")
                user.password = password
                print(f"new password, {user.password}")
            elif choice == 3:
                users.remove(user)
                print("account deleted")
            else:
                break





