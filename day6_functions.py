#functions with variable input
def sum(*n):
    total=0
    for n1 in n:
        total = total + n1
    print(f" the sum of the given numbers is : {total}")

sum()
sum(10)
sum(10,20)
sum(10,20,30,40) 

#
 def f1(n1,*s):
    print(n1)
    for s1 in s:
        print(s1)

f1(10)
f1(10,20,30,40)
f1(10,"A",30,"B")

#
a=10 # global variable
def f1():
    print(a)
    
def f2():
    print(a)
f1()
f2()

#
 def f1():
    a=10
    print(a) # valid

def f2():
    print(a) #invalid

f1()
f2()

#lambda function

s=lambda n:n*n
print("square of 4 is :",s(4))

#
l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1)

#
def IsEven(x):
    if x%2==0:
        return True
    else:
        return False

l=[0,5,10,15,20,25,30]
l1=list(filter(IsEven,l))
print(l1)

#
l=[1,2,3,4,5]
def DoubleIt(x):
    return 2*x

l1=list(map(DoubleIt,l))
print(l1)

#
l=[1,2,3,4,5]
l1=list(filter(lambda x:x*2,l))
print(l1)

#
l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)

#functools module

from functools import*
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result)

from functools import*
result = reduce(lambda x,y:x+y,range(1,101))
print(result)

from functools import*
l=[10,20,30,40,50]
result=reduce(lambda x,y:x*y,l)
print(result)

#math module
import math as m
l=[25,77,54,81,48,34]

def CheckSq(x):
    
    result=m.sqrt(x)
    
    return result
    
    

l1=list(map(CheckSq,l))
print(l1)

#nested function
def outer():
    print("outer function started")
    def inner():
        print("inner")
    print("outer function returning inner")
    return inner

f1 = outer()
f1()

#Decor function

def decor(func):
    def inner(name):
        if name == "sunny":
            print("hello sunny bad morning")

        else:
            func(name)
    return inner
@decor
def wish (name):
    print("hello",name,"Good Morning")

wish("shikhar")
wish("sunny")





