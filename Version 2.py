"""Version with all the Documentation"""
"""In this version, the current issue is that the value of ma and mb are stored, so the user is not prompted again
to input like I would like. We need to figure out how to erase the value of ma and mb while storing it in mc and md."""
import random 

#These are all of the small square boards that make up the big Board 
small0 = [0,1,2,3,4,5,6,7,8]
small1 = [0,1,2,3,4,5,6,7,8]
small2 = [0,1,2,3,4,5,6,7,8]
small3 = [0,1,2,3,4,5,6,7,8]
small4 = [0,1,2,3,4,5,6,7,8]
small5 = [0,1,2,3,4,5,6,7,8]
small6 = [0,1,2,3,4,5,6,7,8]
small7 = [0,1,2,3,4,5,6,7,8]
small8 = [0,1,2,3,4,5,6,7,8]

#This big Board consists of all the small boards which have small boxes 
bigBoard = [small0,small1,small2,small3,small4,small5,small6,small7,small8]

#I killed the firstmove function because we don't need it now. 
"""def firstmove(): #decides which player will get the first move. PlayerA will always be "X" 
# ignore for now   x = raw_input("Enter the name of the first person.")
# ignore for now   y = raw_input("Enter the name of the second person.")
    z = random.choice("AB")
    if z == "A":
           A = int(raw_input("Congrats you are PlayerA. To choose your first big box on the Big Board, please enter a number from 0-8."))
#           B = int(raw_input("To now choose your small box, please enter another number from 0-8."))
           return A
           
    if z == "B":
           A = int(raw_input("Congrats you are PlayerA. To choose your first big box on the Big Board, please enter a number from 0-8."))
#           B = int(raw_input("To now choose your small box, please enter another number from 0-8."))
           return A"""

def moveA(x,y): #PlayerA's moves update the matrices(X)
    """Places a cross on small square y in big square x (or bigBoard[x][y]).  The player only gets to choose the small square,
as the big square location is decided by the previous player's small square location.  In the chance that the big square has been claimed, let's
the player choose another. Updates the list accordingly."""
    bigBoard[x][y] = "X" 
#        print bigBoard[x]
#        return y 


def moveB(x,y): #PlayerB's moves update the matrices (O)
    bigBoard[x][y] = "O"
#        print bigBoard[x]


def winSmall(board, letter): #Checks the small square to see if a player has won. If a player has won the small square, the small board List is replaced with the winning letter in bigBoard Matrix.  
    for i in board: # i = each of the smallboards in bigBoard matrix, so each i is a list 
        if (i[0] == letter and i[1] == letter and i[2] == letter) or (i[3] == letter and i[4] ==letter and i[5] == letter) or (i[6] == letter and i[7] == letter and i[8] == letter) or (i[0] == letter and i[3] == letter and i[6] == letter) or (i[1] == letter and i[4] == letter and i[7] == letter) or (i[2] == letter and i[5] == letter and i[8] == letter) or (i[0] == letter and i[4] == letter and i[8] == letter) or (i[2] == letter and i[4] == letter and i[6] == letter):
            z = board.index(i) 
            board.remove(i)
            board.insert(z, letter)
            return True 
        else:
            return False 


#worried about this function
def winGame(board, letter): #This is the master count of wins.  Checks bigBoard Matrix for a win using a method similar to winSmall. If a winning combination is found, the game ends. 
    if (board[0] == letter and board[1] == letter and board[2] == letter) or (board[3] == letter and board[4] ==letter and board[5] == letter) or (board[6] == letter and board[7] == letter and board[8] == letter) or (board[0] == letter and board[3] == letter and board[6] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[0] == letter and board[4] == letter and board[8] == letter) or (board[2] == letter and board[4] == letter and board[6] == letter):
        if letter == "X":
            print "PlayerA has won the game."
            return True
        if letter == "O":
            print "PlayerB has won the game."
            return True
    else:
        return False 


    
def play(): #The whole game will be under this function call
    moveA(ma,mb) #first player chooses both squares, I should move this function to the top
    while winGame(bigBoard, "X") == False and winGame(bigBoard, "O") == False: 
        while winSmall(bigBoard, "X") == False and winSmall(bigBoard, "O")== False:
            moveB(mc, mb) #second player is prompted using mb but not with mc which held the value 
            moveA(md, mb) #first player now only gets to choose second square 



ma = int(raw_input("Please enter first square"))
mb = int(raw_input("Please enter second square"))
mc = ma
md = mb
   
    
play()
