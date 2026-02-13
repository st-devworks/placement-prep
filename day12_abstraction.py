#abstraction

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


c = Circle(5)
print(c.area())

# Using Method Overriding

class Animal:
    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        return "Meow"


c = Cat()
print(c.sound())

# Using NotImplementedError

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


s = Square(4)
print(s.area())

# Using Interfaces

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
