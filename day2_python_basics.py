#positive or negative

no = int(input("Enter a number :"))
if no > 0 :
    print("number is positive.")
elif no == 0:
    print("no is zero")
else:
    print("no is negative")

# string 
name = input("name : ")
if name == "shikhar":
    print(f"Hello {name}, How are you ?")
else:
    print("hii,how are you ?")

#if else 
marks = int(input("enter your marks :"))
if marks >= 90:
    print("you scored an 'a'")
elif marks >= 75 and marks < 90:
    print("you passed first division")
elif marks > 35 and marks < 75:
    print("you passed the exam")
elif marks > 100 and marks < 0:
    print("invalid input .")
else :
    print("you failed")

#for loop 
for i in range(10):
    print("Shikhar is the best.")

#for imp
name = input("Enter your name :")
x = 0
for i in name:
    print(x,i)
    x = x+1

#leap year
year = int(input("enter the year : "))
if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
    print("it was a leap year .")
else:
    print("not a leap year.")

#Table of numbers 
no = int(input("Enter a number :"))

for i in range(1,11,1):
    print(f"{no} x {i} = {i * no}")

# prime or not
n=int(input("enter a no."))
i=2
if n<=0:
    print(f"{n} is not a prime number")

else:
    while(i<n):
        if(n%i==0):
            print(f"{n} is not a prime number")
            break;
        i+=1
        
        
if(i==n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
    

       
print("loop executed")
