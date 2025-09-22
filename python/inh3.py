class Grandparent:
    def heritage(self):
        print("Family Tradition")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
c.heritage()  # Inherited from Grandparent via Parent
print(isinstance(c,Grandparent))