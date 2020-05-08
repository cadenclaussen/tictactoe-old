import random
import turtle


players = [ '', '' ]
board = [ [ ' ', ' ', ' ' ], [ ' ', ' ', ' ' ], [ ' ', ' ', ' ' ] ]
isWinner = False
isTie = False
currentPlayer = 0
xPlayer = 0


def mainLoop():
    matchStart()
    gameStart()

    render()
    while (isWinner == False and isTie == False):
        getMove()
        render()
        analyze()

    # screen = turtle.Screen()
    # screen.bgcolor("black")
    # pen = turtle.Pen()
    # pen.reset()
    # pen.hideturtle()
    # pen.speed(0);
    # pen.up()


def matchStart():
    global players
    players = [ '', '' ]
    players[0] = input("First player name: ")
    players[1] = input("Second player name: ")


def gameStart():
    global board
    global currentPlayer
    global xPlayer
    board = [ [ ' ', ' ', ' ' ], [ ' ', ' ', ' ' ], [ ' ', ' ', ' ' ] ]
    currentPlayer = random.choice([ 0, 1 ])
    xPlayer = currentPlayer


def gameOver():
    print("The winner is")


def getMove():
    print()

    global players
    global currentPlayer

    # Get the position
    row = int(input(players[currentPlayer] + ": Which row [0, 1, 2]? "))
    column = int(input(players[currentPlayer] + ": Which column [0, 1, 2]? "))

    # Update our model with the move
    if (currentPlayer == xPlayer):
        board[row][column] = 'X'
    else:
        board[row][column] = 'O'

    # Switch players
    if (currentPlayer == 0):
        currentPlayer = 1
    else:
        currentPlayer = 0


def render():
    for row in range(3):
        for column in range(3):
            print(board[row][column], end = "")
            if (column == 0 or column == 1):
                print(" | ", end = "")

        if (row == 0 or row == 1):
            print()
            print("----------")
        else:
            print()


def renderX(x, y):
    print("x");

def renderY(x, y):
    print("y");

def analyze():
    isWinner = False
    isTie = False


mainLoop()
