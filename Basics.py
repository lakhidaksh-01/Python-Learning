import math
print("Hello World")
print(math.floor(3.65))
# print(math.cos(0.5))
'''
this is another way to write a msg
'''

a=1
b=3
c="This is Daksh Lakhi"
d=3.4
print(a+b)
print(c)
print(type(d))


# Strings
str1="this is my first python string"
print(str1[1:6])
print(str1.capitalize())
print(str1.find("this"))
print(str1.upper())
print(str1.lower())
print(str1.count('t'))


# Lists
items=["Harry",2,3,4,5]
items.extend([6,7,8])
print(items)
print(type(items))
items[0]="Daksh"



# Tuples
tup1=(1,2,3)
''' can not be done in tuple tup1[0]=2 '''
print(tup1)

''' 
Note = 1. 'tuple' does not support item assignment but 'list' do support and list is same as array but more powerful i.e. 'list' is mutable and 'tuple' is immutable. 
       2. list can have diffrent muiliple data types but array have only single data type.
'''


# Dictionary
dic1={"name":"Daksh","age":19}
print(type(dic1))
print(dic1)
print(dic1["name"])
dic1["name"]="Lakhi"
dic1["Roll no."]=69
print(dic1.items())
print(dic1.keys())


# Typecasting 
x = 10
y = str(x)  # Convert integer to string
z = float(x) # Convert integer to float
print(y)    # Output: '10'
print(type(y))  # Output: <class 'str'>



list1=[1,2,2,3,4,4,4,5,6,7,8]
s1= set(list1) # Unique values only
print(s1)
# Can also write
set1={1,'name',2,'abc',2}
print(set1)


a=5
b=10
c="Shaurya"
print(str(a)+str(b)+c)
print("10 - 5 is ",10-5)
print("10 * 5 is ",10*5)
print("10 / 5 is ",10/5)
print("10 + 5 is ",10+5)


# Conditional Statements
p=int(input())
print(p)
if(p>4): print("Variable is greater")
elif(p==4): print("Variable is 4")
else: print("Variable is not greater")


# Loops
for i in range(0,11):print(i)

j=0
while(j<15):
    print(j)
    j=j+1


# Functions
''' there are built-in functions can use like print(), len(), type(), range() '''
def average(num1, num2):
    avg=(num1+num2)/2
    return avg

print(average(3,6))

def factorial(n):
    fact=1
    for i in range(1,n+1):fact = fact*i
    return fact

print(factorial(5))


# Recursion : When a function call itself repeatedly
def show(n):
    if(n==0):return
    else:
     print(n) 
     show(n-1)

show(5)


# Exception handling
height=5.10
try:print(height)
except Exception as e: print(e)

try:
    enter=int(input())
    print(enter+3)
except Exception as e:
    print("some error occur",e)


# File I/O in Python : python can be used to perfom operations on a file.(read & write data)
'''
f= open("1.txt","w")
f.write("harry")
f.close()
f= open("1.txt","r")
content = f.read()
f.close()
print(content)

'''


''' NumPy, Pandas, Matplotlib, and Seaborn are the most important Python libraries for getting started with data science. '''