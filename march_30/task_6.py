# Create a base class named Vehicle that has the 
# following attributes: make, model, and year. It 
# should also have a method called get_info() that 
# returns a string with the vehicle's make, model, and 
# year. Then create two subclasses, Car and Truck, 
# that inherit from Vehicle and add additional 
# attributes and methods specific to each type of 
# vehicle.

class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return self.make, self.model, self.year

class Car(Vehicle):

    def __init__(self, make, model, year, tire_size):
        super().__init__(make, model, year)
        self.tire_size = tire_size

    def how_old(self):
        return 2023 - self.year

class Truck(Vehicle):

    def __init__(self, make, model, year, tank_size):
        super().__init__(make, model, year)
        self.tank_size = tank_size

    def days_of_driving(self, kms):
        return self.tank_size / kms

car1 = Car("Hatchback", "Honda", 1999, 15)
print(car1.how_old())

truck1 = Truck("Trash", "Isuzu", 2005, 500)
print(truck1.days_of_driving(100))

