# Class & Object
class Student:
    pass

s1 = Student()

#__init__ constructor
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student("Shikhar", 101)
print(s1.name, s1.roll)

#Modify object data

s1.roll = 102
s1.display()

#Real-world mini example
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.show_balance()

#
class Test:
    x = 10 
    def __init__(self):
        self.y=20

t1=Test()
t2=Test()
print('t1 :',t1.x,t1.y)
print('t2 :',t2.x,t2.y)

#
class Test:
    a=10
    def init (self):
        Test.b=20
    def m1(self):
        Test.c=30
    @classmethod
    def m2(cls):
        cls.d1=40
        Test.d2=400
    @staticmethod
    def m3():
        Test.e=50
print(Test.__dict__)
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.f=60
print(Test.__dict__)

#
class Test:
    a=777
    
    @classmethod
    def m1(cls):
        cls.a=888
    @staticmethod
    def m2():
        Test.a=999
        
print(Test.a)
Test.m1()
print(Test.a)
Test.m2()
print(Test.a)
