logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

goal = random.randint(1,100)

if difficulty == "easy":
    turns = 10
else:
    turns = 5

def turn(x):
    return x-1


should_continue = True
while should_continue:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = turn(turns)
    if turns == 0:
        should_continue = False
        print("You ran out of turns. You lose!")
    if guess < goal:
        print("Too low.")
        print("Guess again.")
    elif guess > goal:
        print("Too high.")
        print("Guess again.")
    else:
        should_continue = False
        print(f"You got it! The answer was {guess}")



