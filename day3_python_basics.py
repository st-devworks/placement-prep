#functions
def wish(name) :
    print("Hello",name,"Good Morning")
a=wish("shikhar")

#finding square
def square(n):
    t=n*n
    return t

square(56)

#addition
def add(x,y):
    sum = x + y
    return sum

x,y = 20,45
add(x,y)

#even or odd
def even_odd(num):
    if num%2 ==0:
        print(num,"is Even Number")
    else:
        print(num,"is Odd Number")
even_odd(10)
even_odd(15)

#factorial
def fact(n):
    
    fact = 1
    
    while n>=1:
        fact=fact*n
        n = n-1
    return fact
for i in range(1,5):
    print("The Factorial of",i,"is :",fact(i)) 

#calculator

def calc(a,b):
    sum=a+b
    print(f"the sum of twoo numbers is : {sum}")
    sub=a-b
    print(f"the substraction of twoo numbers is : {sub}")
    mul=a*b
    print(f"the multiplication of twoo numbers is : {mul}")
    div=a/b
    print(f"the division of twoo numbers is : {div}")
    

n_1,n_2 = map(int,input("enter your numbers :").split())

print(calc(n_1,n_2))

