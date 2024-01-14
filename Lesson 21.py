#Number Guessing Game Objectives:


# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

should_continue=True
continue_game=True

def hint(continue_game):
    players_number = int(input("Please guess a number: "))
    if players_number == guessed_number:
        print(f"Congratulations! You've guessed the correct number, which is {guessed_number}.")
        continue_game=False
    elif players_number < guessed_number:
        print("Too low. Guess again!")
        continue_game=True
    else:
        print("Too high. Guess again!")
        continue_game=True
    return continue_game

while should_continue:
    print("Welcome to the Number Guessing Game!I'm thinking of a number between 1 and 100.")
    guessed_number= random.randint(0,100)
    print(f"Correct answer is {guessed_number}")
    difficulty=input("Choose a difficulty! Easy or Hard:")

    if difficulty=="Easy":
        attempts=10
        while attempts>0 and continue_game:
            print(f"You have {attempts} attempts remaining to guess the number.")
            continue_game=hint(continue_game)
            attempts-=1
    else:
        attempts=5
        while attempts>0 and continue_game:
            print(f"You have {attempts} attempts remaining to guess the number.")
            continue_game=hint(continue_game)
            attempts-=1

    if attempts==0:
        answer=input("You've run out of attempts! Start over? Y or N")
        if answer=="Y":
            should_continue=True
        else:
            should_continue=False
