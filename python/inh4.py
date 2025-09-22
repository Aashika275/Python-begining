class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def give_birth(self):
        print("Mammal gives birth")

class Bird(Animal):
    def lay_eggs(self):
        print("Bird lays eggs")

class Platypus(Mammal, Bird):
    pass

p = Platypus()
p.speak()       # inherited from Animal
p.give_birth()  # inherited from Mammal
p.lay_eggs()  
print(isinstance(p,Mammal))  # inherited from Bird