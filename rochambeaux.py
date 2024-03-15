import random


def rochambeaux():
    hand = ["rock", "paper", "scissors"]
    
    def cpu():
        cpuChoice = random.randrange(0, len(hand))
        return cpuChoice
    
    def player():
        choice = input("rock, paper, or scissors?")
        while choice not in ["rock", "paper", "scissors"]:
            print("please enter a valid hand")
            choice = input("rock, paper, or scissors?")
        return choice
    
    def winCon(playerChoice, cpuChoice):
        if(playerChoice == "rock" and cpuChoice == "scissors"):
            print("Rock crushes scissors, you win!")
        elif(playerChoice == "scissors" and cpuChoice == "rock"):
            print("Rock crushes scissors, you lose...")
        elif(playerChoice == "scissors" and cpuChoice == "paper"):
            print("Scissors cuts paper, you win!")
        elif(playerChoice == "paper" and cpuChoice == "scissors"):
            print("Scissors cuts paper, you lose...")
        elif(playerChoice == "paper" and cpuChoice == "rock"):
            print("Paper covers rock, you win!")
        elif(playerChoice == "rock" and cpuChoice == "paper"):
            print("Paper covers rock, you lose...")
        elif(playerChoice == cpuChoice):
            print("It's a tie!")

    playerHand = player()
    cpuHand = hand[cpu()]
    print(playerHand, cpuHand)
    
    y = input("ROCK PAPER SCISSORS, SHOOT! (press any key)")
    
    winCon(playerHand, cpuHand)

rochambeaux()