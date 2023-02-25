#Python program to convert Celsius to Fahrenheit
c=int(input('enter the value in celsius'))
f=1.8*c+32
print("temperature in f",f)

#to check whether a num is positive,neg,zero
x=int(input("enter the number"))
if(x>0):
    print("num is positive")
elif(x<0):
    print("num is negative")
else:
    print("num is zero")    

#Python Program to Check Prime Number
a=int(input("enter the num"))
flag=0
for i in range(2,a):
    if(a%i==0):
        flag=1
if(flag==0):
    print("num is prime")
else:
    print("num is nor prime")

#Python Program to Print all Prime Numbers in an Interval
flag=0
for i in range(2,100):
    if(i%100==0):
        flag=1
    if(flag==1):
        print(i)

#Program to print prime number in interval
flag=0
for i in range(2,100):
    flag=0
    for j in range(2,i):
        if(i!=j):  
            if(i%j==0):
                flag=1
                break
    if(flag==0):
        print(i)

# Program to make changes in the letter.
letter='''Dear <name>
        you are selected
                on date: <date>'''
name=input("enter the name\n")
date=input("enter the date\n")
letter=letter.replace("<name>",name)       
letter=letter.replace("<date>",date)
print(letter)

# args and kwargs
def fun(*args,**kwargs):
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(key,value)
arg=["name","class","address"]        
kww={"name":"tashu","class":12,"address":"nabha"}
fun(arg,kww)

# Displaying the name
class emp:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def fullname(self):
        print("My name is",self.first,self.last)
ob=emp('anmol','chandan')   
ob.fullname() 

# To make a number divisible by 2 if it is not..
a=int(input("enter the value of a"))
if(a%2==0):
   print("the number is divisible by 2")
elif(a%2!=0):
    a=a*2
    print("the value which after make it divisble by 2 is:",a)   