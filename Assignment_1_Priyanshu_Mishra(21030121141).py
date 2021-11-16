import random

gamechoice=-1
while gamechoice!=0:

    print("Welcome to my GameSpace App!")# This app has 3 games: 1. Rock Paper Scissors, 2. Math Game, 3. Guessing Game.
    print("---------- MENU ----------")
    print("0. Exit App")
    print("1. Rock Paper Scissors")
    print("2. Math Game: Test your problem solving skills")
    print("3. Guessing Game")

    gamechoice=int (input ("Enter Your Choice of Game: "))# Stores what game users want to play.

    if gamechoice==1:
        choice = "z"
        while choice!="n":

            computerscore = 0
            userscore = 0
            numgames = int(input("Welcome to rock, paper, scissors.\nHow many rounds would you like to play?\n"))
            userinput = ""
            computerchoice = ""
            userwin = False
            draw = False
            
            for x in range(0, numgames):
                computerchoice = random.choice(["rock","paper","scissors"])
                userinput = input("Select rock, paper, or scissors\n")

                #to print an error statement in case of an invalid input
                
                while userinput not in ["rock","paper","scissors"]:
                    print("Invalid Input")
                    
                    userinput = input("Select rock, paper, or scissors\n")
                    
                print("You selected",userinput,"and the computer selected",computerchoice+".")

                if userinput == "rock" and computerchoice == "scissors":
                    print("You won this round!")
                    userscore += 1
                elif userinput == "rock" and computerchoice == "paper":
                    print("You lost this round!")
                    computerscore += 1
                if userinput == "paper" and computerchoice == "rock":
                    print("You won this round!")
                    userscore += 1
                elif userinput == "paper" and computerchoice == "scissors":
                    print("You lost this round!")
                    computerscore += 1
                if userinput == "scissors" and computerchoice == "paper":
                    print("You won this round!")
                    userscore += 1
                elif userinput == "scissors" and computerchoice == "rock":
                    print("You lost this round!")
                    computerscore += 1
                if userinput==computerchoice:
                	print("This round was a draw!")
                	
            if userscore > computerscore:
                userwin = True
            elif userscore == computerscore:
                draw = True

            if userwin == True:
                print("Congratulations, you won!\nYour score:",userscore,"\nComputer's score:",computerscore)
            elif draw == True:
                print("You drew!\nYour score:",userscore,"\nComputer's score:",computerscore)
            elif userwin == False:
                print("I'm sorry, but you lost.\nYour score:",userscore,"\nComputer's score:",computerscore)

            choice = str(input("Would you like to play again? y/n\n"))
        
    elif gamechoice==2:
        while True: 
            print("Welcome to Math Game, Test your math skill!")
            print("--- MENU ---")
            print("0. Go back to main menu")
            print("1. Multiplacation")
            print("2. Division")
            print("3. Addition")
            print("4. Substraction")

            operatorchoice = int( input("Enter Your Choice: "))# Stores which math game user wants to play.
            
            if operatorchoice==1:
                multiplicationchoice = -1 #stores the level that user wants to play in multiplication game
                while True:

                    print("Welcome to Multiplication Game!")
                    print("--- Choose Level ---")
                    print("0. Exit")
                    print("1. Beginner")
                    print("2. Intermediate")
                    print("3. Expert")
                
                    multiplicationchoice = int( input("Enter Your Choice: "))
                
                    if multiplicationchoice==1:
                        chances=3
                        number1 = random.randint(1,10)
                        number2 = random.randint(1,10)
                    
                    elif multiplicationchoice==2:
                        
                        chances=2
                        number1 = random.randint(10,50)
                        number2 = random.randint(10,50)
                       
                    elif multiplicationchoice==3:
                        
                        chances=1
                        number1 = random.randint(20,100)
                        number2 = random.randint(20,100)
                                     
                    elif multiplicationchoice==0:
                        print("Exited from Multiplication game!")
                        break
                    else:
                        print("Invalid Choice!")
                    result = number1 * number2
    
                    print(number1 , " * " , number2 , " = ?")
            
                    while chances!=0:
                
                        answer = float(input("Enter your answer: "))
            
                        if answer==result:
                            print("Correct Answer!")
                            break
                        else:
                            print("Incorrect Answer!")
                            chances = chances - 1
                        print("You have ",chances," chances!")
            elif operatorchoice==2:
                divisionchoice = -1
                while True:

                    print("Welcome to Division Game!")
                    print("--- Choose Level ---")
                    print("0. Exit")
                    print("1. Beginner")
                    print("2. Intermediate")
                    print("3. Expert")
                
                    divisionchoice = int( input("Enter Your Choice: "))
                
                    if divisionchoice==1:
                        chances=3
                        number1 = random.randint(1,10)
                        number2 = random.randint(1,10)
                    
                    elif divisionchoice==2:
                        
                        chances=2
                        number1 = random.randint(10,50)
                        number2 = random.randint(10,50)
                       
                    elif divisionchoice==3:
                        
                        chances=1
                        number1 = random.randint(20,100)
                        number2 = random.randint(20,100)
                              
                    elif divisionchoice==0:
                        print("Exited from Division game!")
                        break
                    else:
                        print("Invalid Choice!")
                    result = round(number1 / number2,2)
    
                    print(number1 , " / " , number2 , " = ?")
            
                    while chances!=0:
                
                        answer = float(input("Enter your answer with two decimal values: "))
            
                        if answer==result:
                            print("Correct Answer!")
                            break
                        else:
                            print("Incorrect Answer!")
                            chances = chances - 1
                        print("You have ",chances," chances!")
            elif operatorchoice==3:
                additionchoice = -1
                while True:

                    print("Welcome to Addition Game!")
                    print("--- Choose Level ---")
                    print("0. Exit")
                    print("1. Beginner")
                    print("2. Intermediate")
                    print("3. Expert")
                
                    additionchoice = int( input("Enter Your Choice: "))
                
                    if additionchoice==1:
                        chances=3
                        number1 = random.randint(1,10)
                        number2 = random.randint(1,10)
                    
                    elif additionchoice==2:
                        
                        chances=2
                        number1 = random.randint(10,50)
                        number2 = random.randint(10,50)
                       
                    elif additionchoice==3:
                        
                        chances=1
                        number1 = random.randint(20,100)
                        number2 = random.randint(20,100)
  
                    elif additionchoice==0:
                        print("Exited from Addition game!")
                        break
                    else:
                        print("Invalid Choice!")
                    result = number1 + number2
    
                    print(number1 , " + " , number2 , " = ?")
            
                    while chances!=0:
                
                        answer = int(input("Enter your answer: "))
            
                        if answer==result:
                            print("Correct Answer!")
                            break
                        else:
                            print("Incorrect Answer!")
                            chances = chances - 1
                        print("You have ",chances," chances!")
            elif operatorchoice==4:
                subtractionchoice = -1
                while True:

                    print("Welcome to Subtraction Game!")
                    print("--- Choose Level ---")
                    print("0. Exit")
                    print("1. Beginner")
                    print("2. Intermediate")
                    print("3. Expert")
                
                    subtractionchoice = int( input("Enter Your Choice: "))
                
                    if subtractionchoice==1:
                        chances=3
                        number1 = random.randint(1,10)
                        number2 = random.randint(1,10)
                    
                    elif subtractionchoice==2:
                        
                        chances=2
                        number1 = random.randint(10,50)
                        number2 = random.randint(10,50)
                       
                    elif subtractionchoice==3:
                        
                        chances=1
                        number1 = random.randint(20,100)
                        number2 = random.randint(20,100)
                         
                    elif subtractionchoice==0:
                        print("Exited from Subtraction game!")
                        break
                    else:
                        print("Invalid Choice!")
                    result = number1 - number2
    
                    print(number1 , " - " , number2 , " = ?")
            
                    while chances!=0:
                
                        answer = int(input("Enter your answer: "))
            
                        if answer==result:
                            print("Correct Answer!")
                            break
                        else:
                            print("Incorrect Answer!")
                            chances = chances - 1
                        print("You have ",chances," chances!")
            elif operatorchoice==0:
                print("Exited from Math Game!")
                break
            else:
                print("Invalid Input")
    elif gamechoice==3:
        guesschoice=-1
        print("Welcome to Guessing Game!")
        print("0. Back to main menu")
        print("1. Play")
        guesschoice=int(input("Enter your choice: "))
        while True:

            if guesschoice==1:

                randomnumber = random.randint(0,99)
                for i in range(0,5):
                    chanceleft = 5 - i
                    print("You have",chanceleft,"chances left!")
                    value = int(input("Guess the number between 0 to 99: "))
                    if value < randomnumber:
                        print("Number is greater than the",value)
                    elif value > randomnumber:
                        print("Number is smaller than the",value)
                    else:
                        print("Congratulations!!! You guessed the right number")
                        break
                print("The number was",randomnumber,".")
                guesschoice=int(input("If you would like to exit to main menu, type 0. If you want to keep guessing, type 1: "))
            elif guesschoice==0:
                print("Guessing Game Exited!")
                break #Breaks the loop and exits the game.
            elif guesschoice!=(0,1):
                print("Invalid Input")
                guesschoice=int(input("Enter your choice: "))

#By Priyanshu Mishra