class mammal:
    def walk(self):
        print("walk")   
class dog(mammal):
    def bark(self):
        print("bark")
class cat(mammal):
    def meow(self):
        print("meow")
dog1=dog()
dog1.walk()
print(isinstance(dog1,mammal))
