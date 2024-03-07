from random import randrange

# so yeah im gonna try to make a tic tac toe game that runs in console via text interface

# i suppose the text interface is the last thing that needs to be implemented once the under the hood stuff works, right?

# as well as the gameplay

# so tic tac toe.

# first thing's first, we need a matrix of 3 rows, for 9 panels.
# next, each space needs an id so that players can easily select these spaces. for now, this can just be a list- easy to navigate, and doesn't really have to be connected to the matrix.
# i suppose each space should also have a marker that determines if it's a valid target or not. this CAN be yet another list, since that lets us tie it to the spaceIds later by them sharing indexes.
# additionally we'll have a set of player ids that are preset at 1 and 2. there's really no reason to make it dynamic, since no matter what there's gonna be two players
# even if one of the players is the computer.

# what are the subfunctions that tic tac toe will need?
# turns.
# win and tie detection.
# cpu player?
# draw the game board.
# clear the gameboard

def ticTacToe():
    gameboard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    spaceIds = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ownedSpaces = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    noPlayers = howManyPlayers()
    playerIds = [1, 2]
    

#first function: let's prompt the player to choose whether the game is single or multiplayer.

def howManyPlayers():
    print("Choose whether this will be a single or multiplayer game.")
    playerNum = input("Choose 1 or 2:")
    
    if(playerNum == 1):
        print("Single player mode. You are X.")
        return playerNum
    elif(playerNum == 2):
        print("Multiplayer mode. Player 1 is X, Player 2 is O")
        return playerNum
    else:
        print("Please enter either 1 or 2.")
        howManyPlayers()
    

#second function: let's write something for taking turns.

def turn(currentPlayer, ownedSpaces):
    print("Player {currentPlayer}, go.")
    print("Choose which space you want to fill.")
    space = input("Pick a number from 1 to 9:")
    
    if(space >= 1 and space <= 9 and ownedSpaces[space - 1] == 0):
        ownedSpaces[space - 1] = currentPlayer
        
        return ownedSpaces
    else:
        print("Invalid input.")
        turn(currentPlayer, ownedSpaces)

# the idea here is to keep this function simple. It prompts the current player (whoever's ID is active- will figure that out later) to pick which space they wanna slot their O or X into
# if the space isn't valid, then it keeps harassing them.

def CPUturn(ownedSpaces):
    input("Computer turn.")
    computerSelection = randrange(9)
    
    if(ownedSpaces[computerSelection] == 0):
        ownedSpaces[computerSelection] = 2
        return ownedSpaces
    else:
        CPUturn(ownedSpaces)

# as simple as the computer picks a spot at random. i don't feel like applying actual logic here.