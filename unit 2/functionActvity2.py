# PROBLEM 1
# Create a function that will take in 2 inputs and 
# compare them .
# your input should be number.
# The function should compare if the first imput is 
# less than the second input.
# if it is less than the second input it
# should print true. if it is not, itshould print false 
def compareNumber():
    print("PROGRAM IS RUNNING: please type in a number")
    numA=int(input())
    numB=int(input())
    print(numA < numB)

compareNumber()    

#PROBLEM 2
#create a function that will compare if a student
# has made honor roll
# The student should be able to input2 peices of data
# the first should be their grade and the second should 
# be the number of days they have been absent.
# if the student 's grade is above 90 and the number
# of absenses is less than 5, the program should print
# true, otherwise false 
def honorRoll():
    print("PROGRAM IS RUNNING: please type in your grade")
    grade=int(input())
    print("PROGRAM IS RUNNING: please type in your number of absences")
    absences=int(input())
    print(grade > 90 and absences < 5)