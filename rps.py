# Rock paper scissors game

import random

options = ("rock", "paper", "scissors")

ur_score = 0
comp_score = 0

while ur_score < 3 and comp_score < 3:
    bot = random.choice(options)
    answer = input("Choose an option from Rock, Paper, or Scissors\n").lower() 
    print("You chose", answer)
    print("Computer chose", bot)
    if bot == answer:
        print("draw")
    elif bot == "rock" and answer == "paper" or bot == "paper" and answer == "scissors" or bot == "scissors" and answer == "rock":
        print("you win")
        ur_score += 1
    elif bot == "rock" and answer == "scissors" or bot == "paper" and answer == "rock" or bot == "scissors" and answer == "paper":
        print("you lose")
        comp_score += 1  
    else:
        print("You chose an invalid value. You lose")
    print(f"{ur_score}:{comp_score}")                



