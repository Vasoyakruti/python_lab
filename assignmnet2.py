#1.calculate simple interest
principal = 1000   
rate = 5           
time = 3          

simple_interest = (principal * rate * time) / 100

print("The simple interest is:", simple_interest)

#2.find maximum of two numbers
a = 10
b = 25

if a > b:
    largest = a
else:
    largest = b

print(f"The largest number is: {largest}")

#3.print numbers 1 to 5
for i in range(1,6):
    print(i)
    
#4.find length of a string
string = "Hello, World!"
length = len(string)
print(length)

#5.print a welcome message
print("welcome!")

#6.print first character of a string
my_string = "Hello World!"
print(my_string[0])


#7.print last character of a string
my_string = "Hello World!"
print(my_string[-1])

#8.check positive or negative number
    
number = float(input("Enter a number: "))

if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

#9.add three numbers
num1 = 10
num2 = 20
num3 = 30


sum_of_numbers = num1 + num2 + num3

Display  esult
print(f"The sum of {num1}, {num2}, and {num3} is: {sum_of_numbers}")

#10.take a input from the user
user_input = input("Enter something: ")
print("You entered: " + user_input)

