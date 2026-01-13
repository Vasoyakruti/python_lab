#1.print message
print("hello world")

#2.add two numbers
num1 = float(input("enter a value:"))
num2 = float(input("enter a value:"))
sum = num1+num2
print(f"the sum of {num1} and {num2} is {sum}")

#3.even or odd
num = int(input("enter number:"))
if num % 2 ==0:
    print(f"this number is even")

else:
    print(f"this number is odd")
    
#check leap year
year = int(input("Enter a year:"))

if (year % 4 == 0 and year % 100):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")       
    
#print PI




#store and print constant value
# Store the constant
PI = 3.14159

# Print the constant
print(PI)

    
#square of a number
number = 5
squared_number = number * number
print(squared_number)

#area of a circle
import math

radius = 5
area = math.pi * (radius ** 2)
print(area)

#check data type
x = 5
print(type(x))

y = "Hello"
print(type(y))

#use math function
import math

number = 16
square_root = math.sqrt(number)
print(f"The square root of {number} is {square_root}")

#find power
import math

result = math.pow(2, 3)
print(result)  

#check positive or negative
num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")





    
    