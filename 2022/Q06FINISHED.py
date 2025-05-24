# Q06
import random

def generateWord(pWords):
    # Fully completed function that generates and returns a secret word
    randomNum = random.randint(0,len(pWords)-1)
    secretWord = pWords[randomNum]
    return secretWord

# Add your subprograms here

# sub program to display the remaining attempts
def trackingAttempts(pAttemptsLeft):
    print("-" * 60)
    print("attempts left: ", pAttemptsLeft)
    print("-" * 60)
    return pAttemptsLeft

# sub program to get user input
def gettingInput():
    print("\n \n \n ")
    print("ATTEMPT -", totalAttempts - attemptsLeft + 1)
    print("-" * 60)
    userInput = input("Enter your word: ")
    
    # forcing user to input a word that is same length as the secret word
    while len(userInput) != len(wordToGuess):
        print("-" * 60)
        print("You must enter same length as the secret word!")
        userInput = input("Enter your word:")
        
    return userInput

# subprogram for displaying the stored letters and input
def displayingStoresLetters():
    print("input   |", userInput)
    print("correct |", correctLetters)
    print("wrong   |", wrongLetters)
    print("-" * 60)
    

#---------------------------------------------------------------------------------------
# End of subprograms and start of main program from here

# Array of words
words = ["antelope","ape","badger","bear","beaver","bison","crocodile","elephant",
         "elk","ferret","goat","goose","kangaroo","llama","lion","monkey","moose",
         "orangutan","shark","snake","tiger","whale","wombat"]

# Secret word is generated. 
wordToGuess = generateWord(words)

# Add your main program code here
# initializing variables
wrongLetters = ""
correctLetters = ""
flag = True

# generating attempts
totalAttempts = len(wordToGuess) + 3
attemptsLeft = totalAttempts

print("\nThe number of letters in the secret word: ", len(wordToGuess))
print("You have", attemptsLeft, "attempts to guess.")

# main program loop
while flag and attemptsLeft > 0:
    userInput = gettingInput()
    attemptsLeft -= 1 # Decrease the remaining attempts
    trackingAttempts(attemptsLeft) # Display the updated number of attempts
    
    # If the user guesses the word correctly, end the game
    if userInput == wordToGuess:
        print("\tYOU WON!")
        print("The secret word is", wordToGuess, ".")
        print("Congrats! you have won the game in", totalAttempts - attemptsLeft, "attempts.")
        flag = False
    else:
        # Comparing each character in the user's input to the secret word
        for i in range(len(userInput)):
            if userInput[i] in wordToGuess:  # if the letter is in the secret word
                if userInput[i] not in correctLetters:  # add it to correctLetters if it's not already there
                    correctLetters += userInput[i] + " "
            else:
                if userInput[i] not in wrongLetters: # if the letter is not in the secret word, add it to wrongLetters if it's not already there
                    wrongLetters += userInput[i] + " "
         
        displayingStoresLetters() # display the guessed letters (correct and wrong)

# If the attempts run out, the game is over
if attemptsLeft == 0:
    print("GAME OVER, You lose!")
    print("The secret word is", wordToGuess)
    print("-" * 60)