from art import logo
import random

print(logo)
level = input('Choose your Level : [Easy, Medium, Hard]:').lower()


def easy():
    the_number = random.randint(1, 50)
    print("I am thinking a number between 1 and 50.")
    attempts = 10
    print(f"You have {attempts} attempts left to guess.")
    guess = int(input("Guess a Number: "))
    while attempts > 0:
        attempts -= 1
        if guess == the_number:
            print(f"You guessed it. I was thinking {the_number}.")
            return
        elif guess > the_number:
            print(f"Too High.\nYou have {attempts} attempts left. ")
            guess = int(input("Guess again: "))
        else:
            print(f"Too Low.\nYou have {attempts} attempts left. ")
            guess = int(input("Guess again: "))
    if attempts == 0:
        print(f"You are out of attempts. You couldn't guess the number The number was {the_number}")
        return


def medium():
    the_number = random.randint(1, 100)
    print("I am thinking a number between 1 and 100.")
    attempts = 10
    print(f"You have {attempts} attempts left to guess. ")
    guess = int(input("Guess a Number: "))
    while attempts > 0:
        attempts -= 1
        if guess == the_number:
            print(f"You guessed it. I was thinking {the_number}.")
            return
        elif guess > the_number:
            print(f"Too High.\nYou have {attempts} attempts left. ")
            guess = int(input("Guess again: "))
        else:
            print(f"Too Low.\nYou have {attempts} attempts left. ")
            guess = int(input("Too Low.\nYou have {attempts}attempts left. Guess again: "))
    if attempts == 0:
        print(f"You are out of attempts. You couldn't guess the number The number was {the_number}")
        return


def hard():
    the_number = random.randint(1, 100)
    print("I am thinking a number between 1 and 100.")
    attempts: int = 5
    print(f"You have {attempts} attempts left to guess. ")
    guess = int(input("Guess a Number: "))
    while attempts > 0:
        attempts -= 1
        if guess == the_number:
            print(f"You guessed it. I was thinking {the_number}.")
            return
        elif guess > the_number:
            print(f"Too High.\nYou have {attempts} attempts left. ")
            guess = int(input("Guess again: "))
        else:
            print(f"Too Low.\nYou have {attempts} attempts left. ")
            guess = int(input("Guess again: "))
    if attempts == 0:
        print(f"You are out of attempts. You couldn't guess the number. The number was {the_number}")
        return


if level == "easy":
    easy()
elif level == "medium":
    medium()
elif level == "hard":
    hard()
else:
    print("That's not an option!!!")
