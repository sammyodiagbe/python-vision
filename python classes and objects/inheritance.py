class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        string = 'Your name is {} {}'
        print(string.format(self.firstname, self.lastname))


class Student(Person):
    def __init__(self, firstname, lastname, age):
        super().__init__(firstname, lastname)
        self.age = age