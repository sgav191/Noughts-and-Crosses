import time
import random
print ("Hello and welcome to Noughts & Crosses!")
time.sleep(1)
player1name = input ("What is your name, Player 1: ")
player2name = input ("What is your name, Player 2: ")
print ("Let's see who is going to choose their type of piece!")
input ("Press enter to find out...")
print ("Choosing...")
time.sleep(5)
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
input("Press enter when you're ready to start...")
board = [" "," "," ",
         " "," "," ",
         " "," "," "]
def DrawBoard():
    print (board[0]+"|"+board[1]+"|"+board[2])
    print('-+-+-')
    print (board[3]+"|"+board[4]+"|"+board[5])
    print('-+-+-')
    print (board[6]+"|"+board[7]+"|"+board[8])

DrawBoard()