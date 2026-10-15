# Conditional if/else logic-These are keywords that instruct your
# program to do spesfic instructions based on specfic data

# conditional syntax ( shows how its writtten)










# Using the calculator functions from the calculator.py file,
# Create a main calculator function that uses if/else logic to
# alllow the user to select diffrent arithmethic operations and 
# then peform thoes opperations by running there respective functions.

# Example: an input where if the user enter 1, it will run the additon function.
# 1=addition()
# 2=subtraction()
# 3=multiplication()
# 4= division()

def calculate_add():
    print("Program has started:please type in 2 numbers to add ")
    num1 = int(input())
    num2 = int(input())
    print(num1+num2)
    print("Program has ended.")

def calculate_subtract():
    print("Program has started: please type two numbers to subtract")
    num1 = input()
    num2 = input()
    print(num1-num2)
    print("Program has ended.")

def calculate_multiply():
    print("Program has started: please type two numbers to multiply")
    num1 = input()
    num2 = input()
    print(num1*num2)
    print("Program has ended.")









# choice = input("Please a number")

# if choice =='1':
#     calculate_add()
# elif choice == '2':
#     calculate_subtract()
# elif choice == '3':
#     calculate_multiply()
# elif choice == '4':
#     calculate_divide()

age = int(input())

if age < 7: 
    print(8.00)
elif age > 8 and age < 20:
    print(12.00)
elif age > 21 and age < 60:
    print(20.00)
elif age > 61:
    print(0.00)        

def movieTicket():
    print("Welcome to the movie theater. Please type in your age")
    age = input()
    if age <= 7:
        print("your ticket is 8.00")
    elif age >= 8 and age <= 20:
        print('your ticket is 12.00')
    elif age >= 21 and age <= 60:
        print('your ticket is 20.00')    
    elif age>= 61:
        print("your ticket is free")         
    else:
        print("sorry there was an error in the program....")