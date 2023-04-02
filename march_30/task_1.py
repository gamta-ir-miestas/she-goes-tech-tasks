# Create a class named Car that has the following 
# attributes: make, model, and year. It should also 
# have a method called get_info() that returns a 
# string with the car's make, model, and year.

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return self.make, self.model, self.year

car1 = Car("truck", "MAN", "1994")
print(car1.get_info())