# Q02a

from random import *

#  Initialise variables
counter = 1
answer = randint(0, 10)
guess = 0


#  Print prompt and take guess from user
guess = int(input("Enter a number from 1 to 10:"))


#  Create WHILE loop to check if guess is correct
while guess != answer:
    counter = counter + 1
    if guess > answer:
        print(guess, "was too high. Try again.")
    else:
        print(guess, "was too low. Try again.")

    guess = int(input("Guess again: "))

#  Report the correct answer to the user and indicate the number of guesses
print("You guessed", guess, "in", counter, "guesses.")