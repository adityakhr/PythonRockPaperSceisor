import random
import math
def runProgram():
    userWin=0
    computerWin=0
    options = {1:"Rock", 2:"Paper", 3:"Sceior"}
    while(True):
        input1=input("Enter your choice Rock/Paper/Sceior: ")
        computerChoice = options[math.floor((random.random()*10)%3)+1]
        if input1.upper()=="ROCK" and computerChoice.upper()=="ROCK":
            print("Computer chose to "+options[math.floor((random.random()*10)%2)+1])
            print("Tie")
            print("UserWins="+str(userWin)+" , ComputerWins="+str(computerWin))
        elif input1.upper()=="ROCK" and computerChoice.upper()=="PAPER":
            print("Computer chose to "+options[math.floor((random.random()*10)%2)+1])
            computerWin+=1
            print("Computer Wins")
            print("UserWins="+str(userWin)+" , ComputerWins="+str(computerWin))
        elif input1.upper()=="ROCK" and computerChoice.upper()=="SCEIOR":
            print("Computer chose to "+options[math.floor((random.random()*10)%2)+1])
            print("User Wins")
            userWin+=1
            print("UserWins="+str(userWin)+" , ComputerWins="+str(computerWin))
        elif input1.upper()=="PAPER" and computerChoice.upper()=="PAPER":
            print("Computer chose to "+options[math.floor((random.random()*10)%2)+1])
            print("Tie")
            print("UserWins="+str(userWin)+" , ComputerWins="+str(computerWin))
        elif input1.upper()=="PAPER" and computerChoice.upper()=="SCEIOR":
            print("Computer chose to "+options[math.floor((random.random()*10)%2)+1])
            print("Computer Wins")
            computerWin+=1
            print("UserWins="+str(userWin)+" , ComputerWins="+str(computerWin))
        elif input1.upper()=="PAPER" and computerChoice.upper()=="ROCK":
            print("Computer chose to "+options[math.floor((random.random()*10)%2)+1])
            print("User Wins")
            userWin+=1
            print("UserWins="+str(userWin)+" , ComputerWins="+str(computerWin))
        elif input1.upper()=="SCEIOR" and computerChoice.upper()=="SCEIOR":
            print("Computer chose to "+options[math.floor((random.random()*10)%2)+1])
            print("Tie")
            print("UserWins="+str(userWin)+" , ComputerWins="+str(computerWin))
        elif input1.upper()=="SCEIOR" and computerChoice.upper()=="ROCK":
            print("Computer chose to "+options[math.floor((random.random()*10)%2)+1])
            print("Computer Wins")
            computerWin+=1
            print("UserWins="+str(userWin)+" , ComputerWins="+str(computerWin))
        elif input1.upper()=="SCEIOR" and computerChoice.upper()=="PAPER":
            print("Computer chose to "+options[math.floor((random.random()*10)%2)+1])
            print("User Wins")
            userWin+=1
            print("UserWins="+str(userWin)+" , ComputerWins="+str(computerWin))
        else:
            print("Invalid Input...Thanks for Playing.")
            break 

        input2=input("Do you want play again Yes/No: ")
        if input2.upper()=="YES":
            continue
        elif input2.upper()=="NO":
            print("Thanks for playing")
            break
        else:
            print("Invalid Input...Thanks for Playing.")
            break 

if __name__=="__main__":
    runProgram()