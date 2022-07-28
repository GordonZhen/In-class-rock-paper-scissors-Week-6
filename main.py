
import random

user_action = input("Enter a choice (rock , paper , or scissors:")
possible_action = ("rock" , "paper" , "scissors")
user_computer = random.choice(possible_action)

print(f"\n You chose {user_action}, Computer chose {user_computer}. \n")


