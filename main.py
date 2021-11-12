#Imports
import time
import random
from os import system
#Introduction and Name Entry
system('clear')
print ("Hello and welcome to Noughts & Crosses!")
input("Press enter when you are ready to continue...")
player1name = input ("What is your name, Player 1: ")
player2name = input ("What is your name, Player 2: ")
print ("Let's see who is going to choose their type of piece!")
input ("Press enter to find out...")
print ("Choosing...")
time.sleep(5)
#Set Player Positions
def ChooseSelectPlayer():
    players = ["Player 1","Player 2"]
    selectplayer = random.choice(players)
    return selectplayer
selectplayer = ChooseSelectPlayer()
def GetSelectPlayerName():
    playernames = [player1name,player2name]
    if selectplayer == "Player 1":
        selectplayername = player1name
    else:
        selectplayername = player2name
    return (selectplayername)
selectplayername = GetSelectPlayerName()
print (f"It's you {selectplayername}!!")
ncchoice = input (f"{selectplayername}, what would you like to be (X or O): ")
player1 = ""
player2 = ""
if selectplayer == "Player 1":
    if ncchoice == "X":
        player1 = "Crosses"
        player2 = "Noughts"
    elif ncchoice == "O" or "0":
        player1 = "Noughts"
        player2 = "Crosses"
elif selectplayer == "Player 2":
    if ncchoice == "X":
        player2 = "Crosses"
        player1 = "Noughts"
    elif ncchoice == "0" or "O":
        player2 = "Noughts"
        player1 = "Crosses"

print (f"""Summary:
{player1name} is {player1}
{player2name} is {player2}
""")
input("Press enter when you're ready to start the game...")
system('clear')
#Main Game & CheckWinnerFunction
board = [" "," "," ",
         " "," "," ",
         " "," "," "]
def DrawBoard():
    print (board[0]+"|"+board[1]+"|"+board[2])
    print('-+-+-')
    print (board[3]+"|"+board[4]+"|"+board[5])
    print('-+-+-')
    print (board[6]+"|"+board[7]+"|"+board[8])

def CheckWinner():
    if board[0] == board[1] == board[2]:
        return (True)
    elif board[3] == board[4] == board[5]:
        return (True)
    elif board[6] == board[7] == board[8]:
        return (True)
    elif board[0] == board[3] == board[6]:
        return (True)
    elif board[1] == board[4] == board[7]:
        return (True)
    elif board[2] == board[5] == board[8]:
        return (True)
    elif board[0] == board[4] == board[8]:
        return (True)
    elif board[2] == board[4] == board[6]:
        return (True)
    else:
        return (False)
        
DrawBoard()
gameloop = True
playergo = random.randint(1,2)

while gameloop:
    if playergo == 1:
        player1go = input ("Player 1! It's your go, what is your move: ")
        player1square = int(player1go)-1
        if player1 == "Noughts":
            board[player1square] = "O"
        elif player1 == "Crosses":
            board[player1square] = "X"
        system('clear')
        DrawBoard()
    else:
        player2go = input ("Player 2! It's your go whats your move: ")
        player2square = int(player2go)-1
        if player2 == "Noughts":
            board[player2square] = "O"
        elif player2 == "Crosses":
            board[player2square] = "X"
        system('clear')
        DrawBoard()
    checkwinner = CheckWinner()
    if checkwinner == True:
        gameloop = False
    
    if playergo == 1:
        playergo = 2
    else:
        playergo = 2
    
winner = playergo
if winner == 1:
    winnername = player1name
else:
    winnername = player2name
print (f"The winner is {winnername}! Thanks for playing!")