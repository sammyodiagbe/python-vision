
class Animal:
    def __init__(self,name, category):
        self.name = name
        self.category = category

    def say_something(self,something):
        string = 'You said {}'
        print(string.format(something))
dog = Animal('Johana', 'Sub category')
print(dog.name)
print(dog.category)
dog.say_something('woof woof')