import random

user_action = input("Enter a choice (rock, paper, scissors):")
possible_actions = ["rock" , "paper" , "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

# Use an if... elif... else block to compare choices and determine winner
# By comparing tie conditions first, a lot of cases are counted for.
if user_action == computer_action:
    print(f"Both players selected {user_action}. Wow you tied... lame!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win bro!")
    else:
        print("Paper smothers rock! You dead.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper smothers rock! Winner.")
    else:
        print("Scissors shreds paper! Unlucky")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors shreds paper! Good job dude!")
    else:
        print("Rock smashes scissors! You win bro!")


######

# Continuing we are creating code to allow the task to repeat indefinitely with "whileloop"

import random

while True:
    user_action = input("Enter a choice(rock, paper, scissors):") #Printed for player on screen
    possible_actions = ["rock" , "paper" ,"scissors"] #The possible typed actions
    computer_action = random.choice(possible_actions) #randomises the possible outcomes of the computers action
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n") # "\n....\n" - ??

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:  #Only one else per statement
            print("Paper smothers rock! You dead!")     #If computers choice was paper = Lose (Comparing a tie allows to get another outcome)

    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper smothers rock! Winner!")
        else: 
            print("Scissors shreds paper! Loser!")

    elif user_action == "scissors":
        print("Scissors shreds paper! Good job!")
    else:
        print("Rock smashes scissors! you lose.")

    play_again = input("Play again? (y/n):")
    if play_again.lower() != "y":
        break
             
#continue with bookmark in chrome......
