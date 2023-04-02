# Create a class named Person that has the following 
# attributes: name, age, and address. It should also 
# have a method called get_info() that returns a string 
# with the person's name, age, and address.

class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = str(age)
        self.address = address

    def get_info(self):
        return f"{self.name} is {self.age} years old and lives {self.address}"

person1 = Person("Seven", 15, "Mushroom City")
print(person1.get_info())