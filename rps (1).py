#Ibai
#rps.py
#Play rock paper scissors against the computer

#Init
import random
wins = 0
losses = 0
ties = 0

#Functions
def rps():
    global wins
    global losses
    global ties

    while True:
        player = input("Choose an input (rock, paper, scissors): ")
        if player == "rock" or player == "paper" or player == "scissors":
            computer = random.randint(1,3)
            if computer == 1:
                computer = "rock"
            elif computer == 2:
                computer = "paper"
            else:
                computer = "scissors"
            print(f"\n \n \nYou chose {player}")
            print(f"Computer chose {computer}")
            if player == computer:
                print("It's a tie!")
                ties = ties + 1
            elif player == "rock" and computer == "scissors":
                print("Rock beats scissors! You win!")
                wins = wins + 1
            elif computer == "rock" and player == "scissors":
                print("Rock beats scissors! You lose!")
                losses = losses + 1
            elif player == "paper" and computer == "rock":
                print("Paper beats rock! You win!")
                wins = wins + 1
            elif player == "rock" and computer == "paper":
                print("Paper beats rock! You lose!")
                losses = losses + 1
            elif player == "scissors" and computer == "paper":
                print("Scissors beats paper! You win!")
                wins = wins + 1
            elif player == "paper" and computer == "scissors":
                print("Scissors beats paper! You lose!")
                losses = losses + 1

            print(f"\n \n \nWins: {wins}")
            print(f"Losses: {losses}")
            print(f"Ties: {ties}")
            replay = input("Do you want to play again? (yes,no): ")
            if replay == "no":
                break
        else:
            print("Invalid input")


#Main
rps()
