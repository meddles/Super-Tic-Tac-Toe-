"""Tic Tac Final Here lies all the shit that works. Amen"""

    
import random 


small0 = [0,1,2,3,4,5,6,7,8]
small1 = [0,1,2,3,4,5,6,7,8]
small2 = [0,1,2,3,4,5,6,7,8]
small3 = [0,1,2,3,4,5,6,7,8]
small4 = [0,1,2,3,4,5,6,7,8]
small5 = [0,1,2,3,4,5,6,7,8]
small6 = [0,1,2,3,4,5,6,7,8]
small7 = [0,1,2,3,4,5,6,7,8]
small8 = [0,1,2,3,4,5,6,7,8]

bigBoard = [small0,small1,small2,small3,small4,small5,small6,small7,small8]

def winS(board, letter):
    for i in board:
        if (i[0] == letter and i[1] == letter and i[2] == letter) or (i[3] == letter and i[4] ==letter and i[5] == letter) or (i[6] == letter and i[7] == letter and i[8] == letter) or (i[0] == letter and i[3] == letter and i[6] == letter) or (i[1] == letter and i[4] == letter and i[7] == letter) or (i[2] == letter and i[5] == letter and i[8] == letter) or (i[0] == letter and i[4] == letter and i[8] == letter) or (i[2] == letter and i[4] == letter and i[6] == letter):
            z = board.index(i) 
            board.remove(i)
            board.insert(z, "X")
            return True 
        else:
            return False 

    


def moveA(x,y):
    if type(bigBoard[x][y]) == str:
        y = int(raw_input( "Sorry, please check board for an empty space and choose your small square again."))
        moveA(x,y)
    else:
        del bigBoard[x][y]
        bigBoard[x].insert(y,"X")
        print bigBoard[x]




def moveB(x,y):
    if type(bigBoard[x][y]) == str:
        y = int(raw_input("Sorry, please check baord for an empty space and choose your small square again."))
        moveB(x,y)
    else:
        del bigBoard[x][y]
        bigBoard[x].insert(y,"O")
        print bigBoard[x]

#worried about this function
def winGame(board, letter):
    if (board[0] == letter and board[1] == letter and board[2] == letter) or (board[3] == letter and board[4] ==letter and board[5] == letter) or (board[6] == letter and board[7] == letter and board[8] == letter) or (board[0] == letter and board[3] == letter and board[6] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[0] == letter and board[4] == letter and board[8] == letter) or (board[2] == letter and board[4] == letter and board[6] == letter):
        if letter == "X":
            print "PlayerA has won the game."
        if letter == "O":
            print "PlayberB has won the game."
        

def move(x,y):
    while winGame(bigBoard, "X") == False or winGame(bigBoard, "O") == False: 
        while winS(bigBoard, "X") == False or winS(bigBoard, "O")== False:
            moveA(x,y)
            y = y
            x = int(raw_input("enter second square")) 
            moveB(y, x)
            x = x
            y = int(raw_input("enter the second square"))
    
def first():
#    x = raw_input("Enter the name of the first person.")
#    y = raw_input("Enter the name of the second person.")
    z = random.choice("AB")
    if z == "A":
           Aa = int(raw_input("Congrats you are PlayerA. To choose your first square on the Big Board, please enter a number from 0-8."))
           Bb = int(raw_input("To now choose your small square, please enter another number from 0-8."))
           return Bb
           
    if z == "B":
           Aa = int(raw_input("Congrats you are PlayerA. To choose your first square on the Big Board, please enter a number from 0-8."))
           Bb = int(raw_input("To now choose your small square, please enter another number from 0-8."))
           return Bb

def play():
    move(first(), int(raw_input("enter second square")))
    
play()
