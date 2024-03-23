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
    playerIconRunner = "P"
    playerIconTagger = "O"
    cpuIconRunner = "R"
    cpuIconTagger = "T"
    
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
    
    def gameGeneration(board, cpuDict):
    #player starts as a runner, dead center.
        player = [4, 4, 0]

tag()
