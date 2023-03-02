# наследование

class User:

    def __init__(self, name):
        self.name = name

    def userPrint(self):
        print("user user")


class Student(User):
    def __init__(self, name, id, gpa) :
        super().__init__(name)
        self.id = id
        self.gpa = gpa

    def userPrint(self) :
        print(f"student, id: {self.id}")


user = User("user1")
std = Student("std", 1, 3)
# user.userPrint()
# std.userPrint()

users = [user, std]

b = list(filter(lambda x: type(x) == Student, users))

for item in users:
    if isinstance(item, User):
        item.userPrint()
    else:
        item.userPrint()

