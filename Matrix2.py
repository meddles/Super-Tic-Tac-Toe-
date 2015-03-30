"""Tic Tac Final Here lies all the shit that works. Amen"""

    
import random 

def initBoards():
    global small0 = [0,1,2,3,4,5,6,7,8]
    global small1 = [0,1,2,3,4,5,6,7,8]
    global small2 = [0,1,2,3,4,5,6,7,8]
    global small3 = [0,1,2,3,4,5,6,7,8]
    global small4 = [0,1,2,3,4,5,6,7,8]
    global small5 = [0,1,2,3,4,5,6,7,8]
    global small6 = [0,1,2,3,4,5,6,7,8]
    global small7 = [0,1,2,3,4,5,6,7,8]
    global small8 = [0,1,2,3,4,5,6,7,8]

    global bigBoard = [small0,small1,small2,small3,small4,small5,small6,small7,small8]

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
        bigBoard[x][y] = "X"

def moveB(x,y):
    if type(bigBoard[x][y]) == str:
        y = int(raw_input("Sorry, please check baord for an empty space and choose your small square again."))
        moveB(x,y)
    else:
        bigBoard[x][y] = "O"

def winGameCheck(board, letter):
    """
    Checks to see if the game is won.

    Returns False if not won; else returns 'X' or 'O' depending on the winner.
    """

    if winCheck(bigBoard) == False:
        return False
    elif winCheck(bigBoard) == "X":
        # print "Player A has won the game! Congratulations!"
        return "X"
    elif winCheck(bigBoard) == "O":
        # print "Player B has won the game! Congratulations!"
        return "O"
        
def winCheck(board):
    """
    Checks to see if a board is won. 

    Returns 'X' if won by Player A and 'O' if won by Player B, and False if not yet won.
    """

    # Checks if the input is a list. If not, it has been already won and should return True.
    if isinstance(board,list) == False:
        return True

    # Checks each of the eight possible win conditions.
    elif isinstance(board,list)== True:

        # Checks the horizontal  win conditions.
        if board[0] == board[1] == board[2]:
            if isinstance(board[0],str):
                return board[0]
        elif board[3] == board[4] == board[5]:
            if isinstance(board[3],str):
                return board[3]
        elif board[6] == board[7] == board[8]:
            if isinstance(board[6],str):
                return board[6]

        # Checks the vertical win conditions.
        elif board[0] == board[3] == board[6]:
            if isinstance(board[0],str):
                return board[0]
        elif board[1] == board[4] == board[7]:
            if isinstance(board[1],str):
                return board[1]
        elif board[2] == board[5] == board[8]:
            if isinstance(board[2],str):
                return board[2]

        # Checks the diagonal win conditions.
        elif board[0] == board[4] == board[8]:
            if isinstance(board[0],str):
                return board[0]
        elif board[2] == board[4] == board[6]:
            if isinstance(board[2],str):
                return board[2]
    
    return False

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
