import pet

class Ninja():
    def __init__ (self, first_name, last_name, pet, treats, pet_food):
        self.firstName = first_name
        self.lastName = last_name
        self.pet = pet
        self.treats = treats
        self.petFood = pet_food

    def walk(self):
        print(f"Walking {self.pet.name}")
        self.pet.play()
        return self

    def feed(self):
        print(f"Feeding {self.pet.name} {self.petFood}")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"Bathing {self.pet.name}")
        self.pet.noise()
        return self

dog1 = pet.dog("Champ", "Labrador", ["Sit, Lay, Speak, Roll"], "Bark!")
cat1 = pet.cat("Tangie", "Calico", ["Sit, Lay, Speak, Roll"], "Meow!")
print(dog1.name)
print(cat1.name)
ninja1 = Ninja("Daniel", "Hernandez", cat1 , "Scooby Snack", "chicken")
ninja1.walk()
ninja1.bathe()
ninja1.feed()
cat1.stares()
dog1.drool()
print(cat1.health)
print(dog1.health)