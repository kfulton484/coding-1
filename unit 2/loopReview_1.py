





























def diceGame():
    print("DICE GAME IS RUNNING...")
    print("please type R to rool or Q to quit: ")
    userSelection = input()

    while userSelection != 'q':
        if userSelection == 'r':
            randomNumber = random.randint(1,7)  
            if randomNumber == 7:
                print ("your number is: " + str(randomNumber))
                print("YOU WIN")
                score += 10
                print("score: "+ str(score))
                print("please type R to rool or Q to quit:")
                userSelection = input()
              else:
                print("your number is "+ str(randomNumber))
                print("YOU LOSE")
                score -= 5
                print("score: "+ str(score))
                print("please type r to roll or q to quit:")
                userSelection = input()

        else:
            print("ERROR: Invalid input...")
            print("Please typr R to roll or Q to quit:")
            userSelection = input()
     print("Dice game is off")       