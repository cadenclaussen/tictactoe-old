import random


# This data structure is a two dimensional list that represents a 3 by 3 tic
# tac toe board.  It is initialized with letters to name each of the 9 cells
# in a tic tac toe board to make it easier for a player to select which cell
# to place their X or O.  For example, the top row has cells named a, b, and
# c, going left to right.
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


# Prompt for the player names, as a result of this:
# players[0] should be set to the name of opponent 1
# players[1] should be set to the name of opponent 2
def getPlayerNames():
    global players
    # players[0] = input("First player name: ")
    # players[1] = input("Second player name: ")
    players[0] = "Shane"
    players[1] = "Caden"


# This function should:
# 1. Initialize all the variables for a game
#    - board
# 2. Randomly determine the currentPlayerName
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
# is either players[0] or players[1].  This will be the player that
# moves first.  The player should be chosen randomly.
#
# Set currentPlayerCharacter to "X".  This will be the character of
# the player who is playing first.
def getPlayerStartingGame():
    global currentPlayerName, currentPlayerCharacter
    currentPlayerName = random.choice(players)
    currentPlayerCharacter = "X"


# This function returns a list of all the possible cell names where
# the next move can be made.  This is any cell name in the board list
# of lists that does not contain an "X" or a "Y".
def getPossibleCellNames():
    possibleCellNames = []
    for row in range(3):
        for column in range(3):
            if (board[row][column] != 'X' and board[row][column] != 'O'):
                possibleCellNames.append(board[row][column])
    return possibleCellNames


# Prompt the current player for the cell name they want to move their
# X or O to and then update the board.
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


# For the board list of lists variable, replace the value of
# cellName with the current players character.  For example,
# if the player's character is X, and the cell name is 'a',
# replace the board[row][column] value of 'a' with 'X'.
def updateBoard(cellName, currentPlayerCharacter):
    for row in range(3):
        for column in range(3):
            if (board[row][column] == cellName):
                board[row][column] = currentPlayerCharacter
                return


# Update two variables:
# 1. currentPlayerName
# 2. currentPlayerCharacter
#
# So if players[0] was the currentPlayerName, udpate it to players[1],
# and vice versa.
#
# And, if the currentPlayerCharacter was "X", set it to "O", and vice
# versa.
def nextPlayer():
    global currentPlayerName, currentPlayerCharacter

    if (currentPlayerName == players[0]):
        currentPlayerName = players[1]
    else:
        currentPlayerName = players[0]

    if (currentPlayerCharacter == "X"):
        currentPlayerCharacter = "O"
    else:
        currentPlayerCharacter = "X"


# Returns:
# - True if the board has 3 "X"s or "O"s in a row, column, or diagonally
# - False otherwise
#
# What should be checked here?
# - Check rows 0, 1, 2
# - Check columns 0, 1, 2
# - Check the diagonal upper left to lower right
# - Check the diagonal upper right to lower left
def playerWon():
    for row in range(3):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]):
            return True

    for column in range(3):
        if (board[0][column] == board[1][column] and board[1][column] == board[2][column]):
            return True

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return True

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return True

    return False


# Returns:
# - True if the game is tied
# - False otherwise
#
# A game is tied if all the cells contain an X or an O.
#
# NOTE: This function ONLY needs to determine if the board is full,
# if so, it returns True.  It does not need to determine whether there
# is a winner.
def tieGame():
    for row in range(3):
        for column in range(3):
            if (board[row][column] != 'X' and board[row][column] != 'O'):
                return False
    return True


# This function returns:
# - True if either wins[0] is 2 or wins[1] is 2
# - False otherwise
#
# wins[0] represents the wins by players[0]
# wins[1] represents the wins by players[1]
def matchWinner():
    if (wins[0] == 2):
        return True

    if (wins[1] == 2):
        return True

    return False


# This function renders the tic tac toe board
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


def summarizeTheMatch():
    print()
    print()
    print()
    print("Match summary:")
    print("  " + players[0] + ": " + str(wins[0]))
    print("  " + players[1] + ": " + str(wins[1]))
    print("  Cat: " + str(wins[2]))


main()
