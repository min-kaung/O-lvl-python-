# Q01g

storedLetter = "g"
letter = input("Input a letter ")
# Letter converted to lower case
letter = letter.lower()

# Amend the code by completing the if statement
if letter == storedLetter: 
    print("It is the same letter")
elif letter > storedLetter:
    print("It comes later in the alphabet")
else:
    print("It comes earlier in the alphabet")