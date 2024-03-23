import random

#LET'S DO SOMETHING STUPID
#TAG.
#THE VIDEO GAME.
#THE text based VIDEO GAME

#alright this is very simple.
#there is a large matrix consisting of empty spots. Let's do 7x7.
#the game is measured in "ticks" for each input, and displayed on the matrix. 
#Let's do 8 computer players and 1 human player.
#0s are runners, 1s are taggers. 
#tagging a runner can only be done when the tagger is adjacent to a runner. CPU taggers will ALWAYS tag runners adjacent to them.
#Otherwise, CPUS move randomly. So, we're importing random.
#Players (computer and human) will require three variables that can change: X Position, Y Position, and Tagger?
#These will have to be lists because lists are mutable.

def tag():
    board = [[".",".",".",".",".",".","."], 
             [".",".",".",".",".",".","."], 
             [".",".",".",".",".",".","."], 
             [".",".",".",".",".",".","."], 
             [".",".",".",".",".",".","."], 
             [".",".",".",".",".",".","."], 
             [".",".",".",".",".",".","."]]
    
    #player starts as a runner, dead center.
    player = [0, 4, 4]
    
    def cpuStartGenerator():
        #CPU starting locations should be randomized, but characters cannot occupy the same space. That means that in order to generate starting positions, I need to first generate a set of lists that I add to until the length is equal to the number of CPUs.

        cpuSet = set({(4,4)})
        cpuDict = {0: [1], 1: [0], 2: [0], 3: [0], 4: [0], 5: [0], 6: [0], 7: [0]}
        #the set starts with 4,4 just to prevent cpus from spawing on top of the player.
        
        while len(cpuSet) < 9:
            coords = (random.randrange(0, 7), random.randrange(0, 7))
            cpuSet.add(coords)
        
        #okay so we have a set of unique tuples. Then we have to iterate over the set and each tuple within the set, and add them to the corresponding index in cpuDict.
        #which, not bad but probably slow.
        #however, seems that sets don't have indexes because they're not ordered. So we need a list comprehension first.
        cpuSet.remove((4,4))
        cpuList = [el for el in cpuSet]
        
        for i in range(len(cpuList)):
            for j in cpuList[i]:
                cpuDict[i].append(j)
        
        #alright, this works perfectly now.
        return cpuDict
        
    cpuDict = cpuStartGenerator()
    
    def gameGeneration(board, player, cpuDict):
    
        for key in cpuDict:
            if cpuDict[key][0] == 0:
                board[cpuDict[key][1]][cpuDict[key][2]] = "R"
            else:
                board[cpuDict[key][1]][cpuDict[key][2]] = "T"

        #this should spawn in the CPUs
        if player[0] == 0:
            board[player[1]][player[2]] = "P"
        else: 
            board[player[1]][player[2]] = "O"
        #this should spawn in the player    
        
        return board
    
    board = gameGeneration(board, player, cpuDict)
    
    #okay, now we generate CPUS and create a board.
    #next up: turns.
    #the player has a list of actions:
    #tag an adjacent character
    #or move one tile in any of 8 directions.
    #because the tagger is at a disadvantage, taggers move twice as far with a single movement. 
    #to handle movement, all characters need to be able to detect boundaries of the board. 
    #additionally, for the player, there are less error messages to deal with if it only gives them the option to select choices that are valid.
    #then it's just "invalid selection" for all bad inputs.
    
    #remember: FIRST NUMBER IS Y COORD SECOND IS X COORD
    
    #player turn needs to resolve before NPCs.
    
    def NPCTurn(cpuDict, player):
        #cpu movement rules:
        #generate a number between 0 and 7 for each NPC.
        #this number determines what direction the NPC moves.
        #if the NPC can't move in that direction, it doesn't move this tick.
        #that... should work?
        
        #Update the NPCs.
        for key in cpuDict:
            npcMovement = random.randrange(0, 8)
            if cpuDict[key][0] == 1:
                y = cpuDict[key][1]
                x = cpuDict[key][2]
                
                if (player[1]+1 == y or player[1]-1 == y or player[2]+1 == x or player[2]-1 == x):
                    print("You got tagged!")
                    cpuDict[key][0] = 0
                    player[0] = 1
                    
                    #this should ensure the tagger prioritizes the player
                else:
                    for key2 in cpuDict:
                        if(cpuDict[key2][1]+1 == y or cpuDict[key2][1]-1 == y or cpuDict[key2][2]+1 == x or cpuDict[key2][2]-1 == x):
                            #THAT should work in all cases i think. since any number of these being true passes, it should identify the first character to be next to it
                            print("An NPC got tagged!")
                            cpuDict[key2][0] = 1
                            cpuDict[key][0] = 0
                            break
                        else:
                            if npcMovement == 0 and cpuDict[key][1] > 1:
                                cpuDict[key][1] -= 2
                            elif npcMovement == 1 and cpuDict[key][1] > 1 and cpuDict[key][2] < 6:
                                cpuDict[key][1] -= 2
                                cpuDict[key][2] += 2
                            elif npcMovement == 2 and cpuDict[key][2] < 6:
                                cpuDict[key][2] += 2
                            elif npcMovement == 3 and cpuDict[key][1] < 6 and cpuDict[key][2] < 6:
                                cpuDict[key][1] += 2
                                cpuDict[key][2] += 2
                            elif npcMovement == 4 and cpuDict[key][1] < 6:
                                cpuDict[key][1] += 2
                            elif npcMovement == 5 and cpuDict[key][1] < 6 and cpuDict[key][2] > 1:
                                cpuDict[key][1] += 2
                                cpuDict[key][2] -= 2
                            elif npcMovement == 6 and cpuDict[key][2] > 1:
                                cpuDict[key][2] -=2
                            elif npcMovement == 7 and cpuDict[key][1] > 1 and cpuDict[key][2] > 1:
                                cpuDict[key][1] -= 2
                                cpuDict[key][2] -= 2
            else:
                if npcMovement == 0 and cpuDict[key][1] > 0:
                    cpuDict[key][1] -= 1
                elif npcMovement == 1 and cpuDict[key][1] > 0 and cpuDict[key][2] < 7:
                    cpuDict[key][1] -= 1
                    cpuDict[key][2] += 1
                elif npcMovement == 2 and cpuDict[key][2] < 7:
                    cpuDict[key][2] += 1
                elif npcMovement == 3 and cpuDict[key][1] < 7 and cpuDict[key][2] < 7:
                    cpuDict[key][1] += 1
                    cpuDict[key][2] += 1
                elif npcMovement == 4 and cpuDict[key][1] < 7:
                    cpuDict[key][1] += 1
                elif npcMovement == 5 and cpuDict[key][1] < 7 and cpuDict[key][2] > 0:
                    cpuDict[key][1] += 1
                    cpuDict[key][2] -= 1
                elif npcMovement == 7 and cpuDict[key][2] > 0:
                    cpuDict[key][2] -=1
                elif npcMovement == 7 and cpuDict[key][1] > 0 and cpuDict[key][2] > 0:
                    cpuDict[key][1] -= 1
                    cpuDict[key][2] -= 1
                    
                return [cpuDict, player]
    
    updateList = NPCTurn(cpuDict, player)    
    cpuDict = updateList[0]
    player = updateList[1] 
                         
tag()
