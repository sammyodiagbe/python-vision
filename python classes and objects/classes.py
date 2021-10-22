
class Animal:
    name = ""
    category = ""
    def __init__(self,name, category):
        self.name = name
        self.category = category


dog = Animal('Johana', 'Sub category')
print(dog.name)
print(dog.category)