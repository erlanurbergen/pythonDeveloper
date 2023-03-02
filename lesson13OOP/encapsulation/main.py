# инкапсуляция
from lesson11 import main
from lesson11 import main

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # def getAge(self):
    #     return self.__age
    #
    # def setAge(self, age):
    #     if age <= 0:
    #         print("incorrect data")
    #     else:
    #         self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 0:
            print("incorrect data")
        else:
            self.__age = age

    def printStudent(self):
        print(f"name: {self.__name}, age: {self.__age}")


student = Student("Erlan", 29)
# student.name = " "
# student.age = -99
# student.setAge(10)
student.age = 20
print(student.age)
student.printStudent()