from random import randrange

# so yeah im gonna try to make a tic tac toe game that runs in console via text interface

# i suppose the text interface is the last thing that needs to be implemented once the under the hood stuff works, right?

# as well as the gameplay

# so tic tac toe.

# first thing's first, we need a matrix of 3 rows, for 9 panels.
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
    #gameboard and ownedSpaces could probably be a dictionary to save memory/space/code spaghetti? hm
    gameboard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
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

#ok what's next. win detection? probably win detection.

def winDetector(ownedSpaces):
    #so really this just needs to run after every turn.
    #i just have to check each possible "win" condition and see if a single player owns a series of spaces that indicates victory.
    #or if there's a tie after 9 turns have elapsed.
    #this can be done by iterating over owned spaces and checking if any of the win trios are owned by a single player
    #however there's probably a better way to do this than a million conditionals
    #and also, the last time i tried a million conditionals it just broke
    #i can probably make a list or a dictionary of win conditions
    #win conditions being...
    #0 1 2, 3 4 5, 6 7 8, 0 3 6, 1 4 7, 2 5 8, 0 4 8, and 2 4 6.
    #since ownedspaces holds data for which player has which space...
    #how to check the IDs in a reasonable way that doesn't go back to the "million conditionals"?
    #i could make a dictionary with the ids 0, 1, and 2, corresponding to empty lists.
    #iterate over owned spaces, storing each space's id into the corresponding dictionary index
    #once done, I can check the dictionary indices against the win conditions, with an index containing any of the three ids matching a win condition moving to a victory function
    #if no win condition is found but all spaces are owned, it moves to a tie function
    #otherwise the game continues
    #yeah this could work
    #...just pseudocode for rn tho because my head is kinda fuzzy and im not feelin great today
    winConditions = {
        0 : [0, 1, 2],
        1 : [3, 4, 5],
        2 : [6, 7, 8],
        3 : [0, 3, 6],
        4 : [1, 4, 7],
        5 : [2, 5, 8],
        6 : [0, 4, 8],
        7 : [2, 4, 6]
    }
    
    playerOwnedSpaces = {
        0 : [],
        1 : [],
        2 : []
    }
    
    checker = False
    
    for i in ownedSpaces:
        playerOwnedSpaces[ownedSpaces[i]].append(i)
        
    for key in winConditions:
        if (all(ele in playerOwnedSpaces[1] for ele in winConditions[key])):
            checker = True
            victoryPrintout(1)
        elif (all(ele in playerOwnedSpaces[2] for ele in winConditions[key])):
            checker = True
            victoryPrintout(2)
        else:
            return
        
    if (checker == False and (not 0 in ownedSpaces)):
        tiePrintout()
    else:
        return
    
def victoryPrintout(player):
    print("Player " + str(player) + " Wins!")
    input("Would you like to play again? Y/N")

def tiePrintout():
    None
    
#actually with all this stuff it should be pretty easy to finish tbh
#but i dont wanna do it tonight so this is just me putting something here to commit and hit the github commits goal tonight
#that way i can work tomorrow mornign wthout worry

#WHOOPS THIS WEEK KILLED ME

#the recursive inputs break so i'm gonna have to go back and fix those

#UGH actually i hate this. im gonna do something else more fun. 