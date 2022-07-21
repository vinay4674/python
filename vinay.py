'''print('Hello world')
a=10
b=20
print(a+b)

vinay=int(input("enter a value"))
print(type(vinay))
print(type(int(vinay**0.5)))

hight=10
base=16
area=(hight*base)/2
print(area)'''
'''
#program to solve quedratic equaction
#quedratic equaction ax*2+bx+c
#formula for quedratic equaction -b+(b**2-4ac)*0.5/2a
#using the "import cmath" module
#we are using varibles a,b,c,d and sol1
#we can seprate formula (b**2)-(4ac) then declare the varible
#print the sol1
import cmath
a=2
b=4
c=6
#equaction=-b+(b*2 - 4*a*c)*0.5
#quedratic=equaction/2*a
#print(quedratic)

d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
print(sol1)
'''
#program to swape two varibles
'''
a=5
#print(a)
b=6
#print(b)
c=a
a=b
b=c
print(a)
print(b)'''
#program to genrate prime number
'''
value=int(input("enter the values"))
if (random!=1):
	print("it is not a prime  number")
elif(random==0):
	print('it is not a prime number')
#else:
#	print('it is prime number')
'''
#program to generate random number
'''
import random

print(random.randint(0,3))
'''
#progran to convert kilometer to miles
'''
kilometer=int (input('enter the value'))
print(type(kilometer))
converction=0.621371
miles=kilometer*converction
print(miles)
'''
# to convert celsus to fahrenit
'''
celsius=37.5
fahrenit=(celsius*1.8)+32
print(fahrenit)'''

#program to check number is positive negative or 0
#define a varible and give a number to that varible
#create the if and else condition to chaeck the value is true or false
#if condition satisify then function is execute
'''
number= int(input('enter a number'))
if (number>0):
	print("it is a positive nmber",number)

elif(number==0):
	print("it is a equal to zero ",number)
else:
	print("it is a negative nuber",number)'''


#program to check if number is odd or even
#first take a varible for input enter the numbers through input device
#write the condition if it satisify the condition
# goes  to print statement and print the values
'''
num=int(input("enter the nmber"))
if (num%2)==0:
	print('number is even',num)
else:
	print('number is odd ',num)
'''
#program to check the leap year
#every year is divide by 4 then it is a leap year
'''
year=int (input("enter the year"))
if (year%4)==0:
	print("it is a leap year",year)
else:
	print("it is not leap year",year)'''
#program to find largest amount of three number
'''

a=int(input("enter the value of a "))
b=int(input("enter the value of b "))
c=int(input("enter the value of c "))
if (a>b) and (a>c):
	print("a is  largest amount",a)
elif (b>a) and (b>c):
	print("b is the largest amount",b)
else:
	print("c is a largest number",c)

'''
for i in range(10):
	print(i)
	if i==1:
		break
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
