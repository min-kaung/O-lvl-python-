# Q04c

def genNewKey (pString, pNum):
    newKey = ""        # Make new word here

    # Write your code below this line
    newKey = pString[:2] + str(pNum) + pString[2:]
    
    return newKey

myString = input ("Enter a string: ")
myNumber = int (input ("Enter a whole number: "))

if (len (myString) != 4):
    print ("String must be four characters")
else:
    print ("Original: ", myString, myNumber)

    # Complete the call to the subprogram
    myNewKey = genNewKey(myString, myNumber)
    print ("New word:", myNewKey)

