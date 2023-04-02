# Create a class named Rectangle that has the following 
# attributes: width and height. It should also have 
# methods called area() and perimeter() that return 
# the area and perimeter of the rectangle, respectively.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

rectangle1 = Rectangle(5, 8)
print(rectangle1.area())
print(rectangle1.perimeter())