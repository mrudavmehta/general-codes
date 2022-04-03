import random

def PrintBoard(board):
    print(board[1],"|",board[2],"|",board[3],sep="")
    print("-----")
    print(board[4],"|",board[5],"|",board[6],sep="")
    print("-----")
    print(board[7],"|",board[8],"|",board[9],sep="")

def PlayerLetter():
    while True:
        letter=input("Do you want to be X or O? ")
        letter=letter.upper()
        if letter=="X":
            return {"player":"X","computer":"O"}
        elif letter=="O":
            return {"player":"O","computer":"X"}
        else:
            print("Invalid option, try again")

def First():
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return "player"

def PlayAgain():
    ans=input("Do you want to play again? ")
    return ans.lower().startswith("y")

def Winner(board,le):
    return ((board[7] == le and board[8] == le and board[9] == le) or # across the top
    (board[4] == le and board[5] == le and board[6] == le) or # across the middle
    (board[1] == le and board[2] == le and board[3] == le) or # across the boardttom
    (board[7] == le and board[4] == le and board[1] == le) or # down the left side
    (board[8] == le and board[5] == le and board[2] == le) or # down the middle
    (board[9] == le and board[6] == le and board[3] == le) or # down the right side
    (board[7] == le and board[5] == le and board[3] == le) or # diagonal
    (board[9] == le and board[5] == le and board[1] == le))

def GetPlayerMove(board):
    while True:
        move=int(input("What is your next move?(1-9) "))
        if move in PossibleMoves and move in [1,2,3,4,5,6,7,8,9]:
            return move

def GetComputerMove(board):
    Corners=[]
    Sides=[]
    #Next move computer win possible
    for i in PossibleMoves:
        copy=board.copy()
        copy[i]=DP["computer"]
        if Winner(copy,DP["computer"]):
            return i
    #Next move player win possible
    for i in PossibleMoves:
        copy=board.copy()
        copy[i]=DP["player"]
        if Winner(copy,DP["player"]):
            return i
        #Checking corners
    for i in PossibleMoves:
        if i in [1,3,7,9]:
            Corners.append(i)
        elif i==5:
            Center=5
        elif i in [2,4,6,8]:
            Sides.append(i)
    if not Corners==[]:
        return random.choice(Corners)
    else:
        return 5
    if not Sides==[]:
        return random.choice(Sides)

#-------MAIN PROGRAM----------------------------------------------------------------------------
print("Welcome to Tic Tac Toe!")
print("Guide:")
print("1|2|3")
print("-----")
print("4|5|6")
print("-----")
print("7|8|9")
while True:
    board=[" "]*10
    DP=PlayerLetter()
    turn = First()
    PossibleMoves=[]
    for i in range(1,10):
        if board[i]==" ":
            PossibleMoves.append(i)
    print("The",turn,"will go first")
    GameIsPlaying=True
    while True:
        if turn=="player":
            PrintBoard(board)
            move=GetPlayerMove(board)
            board[move]=DP["player"]
            PossibleMoves.remove(move)
            if Winner(board,DP["player"]):
                PrintBoard(board)
                print("Hooray! You Have Won the Game!! ",end="\n\n")
                break
            else:
                if PossibleMoves==[]:
                    PrintBoard(board)
                    print("The game is a Tie!",end="\n\n")
                    break
                else:
                    turn="computer"
           
        else:
            move=GetComputerMove(board)
            board[move]=DP["computer"]
            PossibleMoves.remove(move)
            if Winner(board,DP["computer"]):
                PrintBoard(board)
                print("The computer has beaten you! You lose!,",end="\n\n")
                break
            else:
                if PossibleMoves==[]:
                    PrintBoard(board)
                    print("The game is a Tie!",end="\n\n")
                    break
                else:
                    turn="player"
    if not PlayAgain():
        break