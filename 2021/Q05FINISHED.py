#      Q05

def displayMenu():
     # Completed subprogram that displays the menu
    
    print("                  Menu                    ")
    print("------------------------------------------")
    print("[1] Add player name")
    print("[2] Play guess the capital city")
    print("[3] End game")
    print("------------------------------------------")

def getMenuChoice():
    # Completed subprogram that gets and validates the menu choice
    choices = [1,2,3]
    mChoice = 0
    
    # Menu choice is validated
    while mChoice not in choices:
        mChoice = int(input("Input your menu choice: "))

    # Valid menu option returned to the main menu
    return mChoice
     
def addPlayerName():
    # Add your code to:
    #   ensure a player name is input
    #   return the player name to the main menu
    pName = ""
    while pName == "":
        pName = input("Enter player name: ")  

    return pName


def guessCapital():
    # Partially completed subprogram to:
    #   display questions
    #   check guesses
    #   return final score
    
    # Arrays holding question numbers, countries and their capital cities
    questions = [1,2,3,4,5,6,7,8,9]
    countries = ["England","France","Spain","Italy","Germany","Scotland","Wales","United Arab Emirates","China"]
    capitals = ["London","Paris","Madrid","Rome","Berlin","Edinburgh","Cardiff","Abu Dhabi","Beijing"]

    questionCount = 1
    questionScore = 0

    # Add your code here
    selected_questions = []
    while questionCount < 6:
        question_number = int(input("Enter a question number(1-9): "))
        while not ( 1 <= question_number <= 9):
            question_number = int(input("You must enter a question number(1-9): "))
        question_number = question_number - 1
        
        
        if question_number not in selected_questions:
            questionCount += 1
            selected_questions.append(question_number)
            print("What is the capital city of ", countries[question_number], "?")
            answer = input("Answer: ").lower()
            
            if answer == capitals[question_number].lower():
                questionScore += 1
                print("Correct! \n")
            else:
                print("Incorrect! The capital of", countries[question_number], "is", capitals[question_number], "\n")
        else:
            print("It is already answered. Enter another \n")
        
    return questionScore

menuChoice = 0
score = 0
playerName = ""

while menuChoice != 3:
    displayMenu()
    menuChoice = getMenuChoice()
    
    # Add your code to:
    #   call the relevant subprogram if the menu choice is 1 or 2
    #   display the player name and the score if the menu choice is 3
    if menuChoice == 1:
        playerName = addPlayerName()
    elif menuChoice == 2:
        score = guessCapital()
    elif menuChoice == 3:
        print("Name: ", playerName)
        print("Score: ", score)
        
