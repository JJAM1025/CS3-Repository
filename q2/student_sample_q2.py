class Student:
    __name: str
    __age = 0
    def __init__(self, name):
        self.__name = name
    def set_age(self, age):
        if age > 0:
            self.__age = age
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
    def greet(self):
        return f"Hi! My name is {self.__name}."
    def set_name(self,name):
        self.__name = name

student1 = Student("Je")
student1.set_age(14)
student1.set_name("Je")
print("Student name: ", student1.get_name())
print("Student age: ", student1.get_age())
print(student1.greet())
