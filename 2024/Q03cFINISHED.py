# Q03c

# Complete the line to take a string input
aString = input("Enter a string: ")

# Complete the selection statement
if (aString != ""):

    # Convert the string to an integer
    aNum = int(aString)

    if (aNum > 0):
    
        # Complete the test
        if (1 <= aNum <= 20) or (aNum >= 60):
            print ("Acceptable")
        # Complete the test            
        elif (aNum >= 31) and (aNum <= 39):
            print ("Centre")
        # Complete the test            
        elif (aNum == 30):
            print ("Perfect")
        else:
            print ("No message")
    else:
        print ("The number must be greater than zero")
else:
    print ("You must provide a number")



 
    