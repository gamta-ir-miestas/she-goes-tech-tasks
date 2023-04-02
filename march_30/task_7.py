# Create a base class named Person that has the 
# following attributes: name, age, and address. It 
# should also have a method called get_info() that 
# returns a string with the person's name, age, and 
# address. Then create two subclasses, Student and 
# Teacher, that inherit from Person and add additional 
# attributes and methods specific to each role.

class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = str(age)
        self.address = address

    def get_info(self):
        return f"{self.name} is {self.age} years old and lives {self.address}"

class Student(Person):

    def __init__(self, name, age, address, major, grade):
        super().__init__(name, age, address)
        self.major = major
        self.grade = grade

    def dream_grade(self, dream):
        if dream > self.grade:
            return "Work on for that grade! You can do it!"
        elif dream == self.grade:
            return "You reached your dream grade!"
        return "You surpassed you dream grade! Wow!"

class Teacher(Person):

    def __init__(self, name, age, address, major, students):
        super().__init__(name, age, address)
        self.major = major
        self.students = students

    def overworked(self):
        if self.students > 25:
            return "The teacher is overworked"
        return "The teacher is not overworked"

student1 = Student("Max", 16, "Frog City", "Physics", 9)
print(student1.dream_grade(8))

teacher1 = Teacher("Suzy", 51, "City of Dreams", "Maths", 27)
print(teacher1.overworked())