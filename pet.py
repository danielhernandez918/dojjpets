class pet:
    def __init__ (self, name, type, tricks,  pet_sound):
        self.name = name
        self.type =type
        self.tricks = tricks
        self.sound = pet_sound
        self.health = 50
        self.energy = 50

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(self.sound)
        return self

class cat(pet):
    def __init__ (self, name, type, tricks,  pet_sound):
        super().__init__(name, type, tricks,  pet_sound)
    def sleep(self):
        super().sleep()
    def eat(self):
        super().eat()
    def play(self):
        super().play()
    def noise(self):
        super().noise()
    def stares(self):
        print("stares")

class dog(pet):
    def __init__ (self, name, type, tricks,  pet_sound):
        super().__init__(name, type, tricks,  pet_sound)
    def sleep(self):
        super().sleep()
    def eat(self):
        super().eat()
    def play(self):
        super().play()
    def noise(self):
        super().noise()
    def drool(self):
        print("drools")


# dog1 = dog("Champ", "Labrador", ["Sit, Lay, Speak, Roll"], "Bark!")
# cat1 = cat("Tangie", "Calico", ["Sit, Lay, Speak, Roll"], "Meow!")
# print(cat1.name)
# print(dog1.name)
# cat1.noise()
# dog1.noise()
# cat1.play()
# print(cat1.health)
# cat1.stares()