# loop- a loop is a construct that repeats its self (special function)
# In programing, a loop allows to repeat code instructions.

# there are two types of loops : for loop and while loop

#While loop - a type of loop where so long as a condition is equal 
# to true it will keep running forever .

# the keyword is while --> do while 

# syntax
num = 4
while 2+2 == num: # condition --> operations - must be true 
    #print(num==4)
    print("the program is running..")
    num = input("please type in a new number")

# while loops WILL ALWAYS run unless you change the condition 
# we can do this by writing instructions to manually change. 

def passwordReset():
    correctPw = "1234zyx"
    userPwAttempt = input(4)

    print("Please log in with your password")
    userPwAttempt = input

    while userPwAttempt != correctPw:
        print("sorry incorrect Password")
        print("Please try again")
        attempts-= 1
        print('number of attempts left : '+ str(attempts))
        userPwAttempt = input()
    print("Welcome you have access")


    def vending_machine():
    # Dictionary mapping the item codes to the product names
    inventory = {
        "B3": "Nacho Chips",
        "G4": "BBQ Chips",
        "G7": "Plain Chips",
        "D3": "Water",
        "G5": "Cola Soda"
    }
    
    print("--- Vending Machine Menu ---")
    for code, item in inventory.items():
        print(f"[{code}] {item}")
    print("----------------------------")

    while True:
        # Prompt the user for an item selection or to quit
        user_input = input("\nEnter a vending machine code (or 'q' to quit): ").strip().upper()
        
        # Check if the user wants to quit
        if user_input == 'Q':
            print("Thank you for using the vending machine. Goodbye!")
            break
            
        # Check if the entered code exists in the machine
        if user_input in inventory:
            print(f"Dispensing: {inventory[user_input]}")
        else:
            print("Invalid code. Please try again or press 'q' to quit.")
