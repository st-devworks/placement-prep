Method Overriding

class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


animals = [Dog(), Cat()]

for a in animals:
    a.sound()

Operator Overloading

print(5 + 3)        # addition
print("Hi " + "You")  # string concatenation

print(5 + 3)        # addition
print("Hi " + "You")  # string concatenation

Function Polymorphism (Duck Typing)

class Bird:
    def fly(self):
        print("Bird flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def flying_test(obj):
    obj.fly()

flying_test(Bird())
flying_test(Airplane())


