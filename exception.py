try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1/num2

except ZeroDivisionError:
    print("you cannot divide by zero!")

except ValueError:
    print("please enter valid number!")

else:
    print("Division successfull result is:",result)

finally:
    print("This block always runs.")  
    
                  
#ex-2
try:
    my_list = [1,2,3]
    print(my_list[1])

except IndexError:
    print("Index is out of range")

else:
    print("Element found successfully")

finally:
    print("Program finished")    