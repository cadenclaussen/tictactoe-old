import random


# NOTE: DO NOT EDIT ANY OF THESE LINES DEFINING THE GLOBAL VARIABLES

# This data structure is a two dimensional list that represents a 3 by 3 tic
# tac toe board.  It is initialized with letters to name each of the 9 cells
# in a tic tac toe board to make it easier for a player to select which cell
# to place their X or O.  For example, the top row has cells named a, b, and
# c, going left to right.
# 
# Here is a visual example of a rendered board with the cell names where an
# X or an O can be played:
#
#   a  |  b  |  c
# -----------------
#   d  |  e  |  f
# -----------------
#   g  |  h  |  i
#
board = [ [ 'a', 'b', 'c' ], [ 'd', 'e', 'f' ], [ 'g', 'h', 'i' ] ]

# This is a list of the two player names
players = [ '', '' ]

# This is the name of the player who is starting the game
playerStartingGame = ''

# The name of the player whose move it is (either players[0] or players[1])
currentPlayerName = ''

# The character of the player whose move it is (either X or O)
currentPlayerCharacter = ''

# This array contains wins for each player
# - wins[0] contains the wins for players[0]
# - wins[1] contains the wins for players[1]
# - wins[2] contains the ties (or wins for the Cat)
wins = [ 0, 0, 0 ]



# This is the main loop (or controller) for the match.
# A match is over when one of the two opponents wins 3 games.
#
# NOTE: DO NOT CHANGE
def main():

    getPlayerNames()
    while (matchWinner() == False):

        initializeGame()
        renderTheBoard()
        while (playerWon() == False and tieGame() == False):
            getCurrentPlayersMove()
            renderTheBoard()
            if (playerWon() == False and tieGame() == False):
                nextPlayer()

        summarizeTheGame()
        summarizeTheMatch()



# Prompt for the player names, as a result of this, the global
# variable named players should get updated:
# - players[0] should be set to the name of opponent 1
# - players[1] should be set to the name of opponent 2
#
# NOTE: ADD CODE HERE!!!
def getPlayerNames():
    global players
    players[0] = input("first player name? ")
    players[1] = input("second player name? ")



# NOTE: DO NOT CHANGE
def initializeGame():

    # Reset the board
    global board
    board = [ [ 'a', 'b', 'c' ], [ 'd', 'e', 'f' ], [ 'g', 'h', 'i' ] ]

    # Print some information so its clear we are starting a new game
    print()
    print()
    print()
    print("New Game!")
    print()

    # Randomly get the player starting the game
    getPlayerStartingGame()



# This function should set two global variables:
# 1. currentPlayerName
# 2. currentPlayerCharacter
#
# Set currentPlayerName to the name of one of the two players, which
# is the value of either players[0] or players[1].  The player should
# be chosen randomly.  This player will move first in the new game.
#
# Set currentPlayerCharacter to "X".  This will be the character of
# the player who is moving first.
#
# NOTE: ADD CODE HERE!!!
def getPlayerStartingGame():
    global currentPlayerName, currentPlayerCharacter
#  startPlayerName = random.choice(player1, player2)


# This function returns a list of all the possible cell names where
# the next move can be made.  This is any value in the global
# variable "board" that does not contain an "X" or a "Y".
#
# NOTE: ADD CODE HERE!!!
def getPossibleCellNames():

    # Initialize the list
    possibleCellNames = []

    # IMPLEMENT HERE to determine all the remaining possible cell names

    # Return the list of possible cell names
    return possibleCellNames



# Prompt the current player for the cell name where they want to place
# their "X" or "O".  Afterwards, update the 'board" global variable.
#
# NOTE: DO NOT CHANGE
def getCurrentPlayersMove():
    print()
    possibleCellNames = getPossibleCellNames()
    possibleCellNamesCommaSeparated = ", ".join(possibleCellNames)
    while True:
        cellName = input(currentPlayerName + " (" + currentPlayerCharacter + ") (" + possibleCellNamesCommaSeparated + ")? ")
        if ((cellName in possibleCellNames) == False):
            print("Invalid cell name: " + cellName)
            continue
        break
    updateBoard(cellName, currentPlayerCharacter)



# For the global "board" variable, replace the value of
# the cell name with the current player's character.  For
# example, if the player's character is X, and the cell
# name is 'a', replace the board[row][column] value that
# contains an 'a' with the character 'X'.
#
# NOTE: ADD CODE HERE!!!
def updateBoard(cellName, currentPlayerCharacter):
    global board
    


# Update two variables:
# 1. currentPlayerName
# 2. currentPlayerCharacter
#
# If players[0] was the currentPlayerName, udpate it to players[1],
# and vice versa.
#
# and...
#
# If the currentPlayerCharacter was "X", set it to "O", and vice
# versa.
#
# NOTE: ADD CODE HERE!!!
def nextPlayer():
    global currentPlayerName, currentPlayerCharacter



# Returns:
# - True if the board has 3 "X"s or "O"s in a row, column, or diagonally
# - False otherwise
#
# What should be checked here?
# - Check rows 0, 1, 2 for the same X or O
# - Check columns 0, 1, 2 for the same X or O
# - Check the diagonal upper left to lower right
# - Check the diagonal upper right to lower left
#
# NOTE: ADD CODE HERE!!!
def playerWon():
    return False



# Returns:
# - True if the game is tied
# - False otherwise
#
# A game is tied if all the the values of the "board" global variable
# contain an "X" or an "O".
#
# NOTE: This function ONLY needs to determine if the board is full, if
# so, it returns True.  It does not need to determine whether there is
# a winner.
#
# NOTE: ADD CODE HERE!!!
def tieGame():
    return False



# This function returns:
# - True if either wins[0] is 2 or wins[1] is 2
# - False otherwise
#
# Note:
# - wins[0] represents the wins by players[0]
# - wins[1] represents the wins by players[1]
#
# NOTE: ADD CODE HERE!!!
def matchWinner():
    return False



# This function renders the tic tac toe board
#
# NOTE: DO NOT CHANGE
def renderTheBoard():
    print()
    print()
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



# NOTE: DO NOT CHANGE
def summarizeTheGame():
    print()

    if (tieGame()):
        print("Cat won the game!")
        wins[2] += 1
        return

    print(currentPlayerName + " won the game!")
    if (players[0] == currentPlayerName):
        wins[0] += 1
    else:
        wins[1] += 1



# NOTE: DO NOT CHANGE
def summarizeTheMatch():
    print()
    print()
    print()
    print("Match summary:")
    print("  " + players[0] + ": " + str(wins[0]))
    print("  " + players[1] + ": " + str(wins[1]))
    print("  Cat: " + str(wins[2]))



main()