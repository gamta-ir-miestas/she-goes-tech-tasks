# Create a class named Animal that has the following 
# attributes: name and species. It should also have a 
# method called speak() that returns a string with the 
# animal's sound.

class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species.lower()
        self.sounds = {"cat": "meow", "dog": "woof", "bird": "chirp", "horse": "neigh", "pig": "oink", "goat": "baa", "sheep": "baa", "cow": "moo", "donkey": "hee-haw", "chicken": "cluck", "wolf": "awoo", "fox": "WHAT DOES THE FOX SAY? RING DING DING", "frog": "ribbit", "lion": "roar"}
    
    def speak(self):
        if self.species in self.sounds:
            return self.sounds[self.species]
        return "Sorry, I have no idea of how this animal sounds"

animal1 = Animal("Cleo", "cat")
print(animal1.speak())
animal2 = Animal("Mimi", "fox")
print(animal2.speak())
animal3 = Animal("Kim", "zebra")
print(animal3.speak())