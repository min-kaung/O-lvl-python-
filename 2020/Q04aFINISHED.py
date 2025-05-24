#   Q4aFINISHED

#   Initialise variables
#   Data format: First name, Last name, English test mark, Maths test mark

studentTestScores = [
["Kevin", "Horney", 71, 55],
["Tony", "Tison", 36, 50],
["David", "Smith", 39, 48],
["Vicky", "Bertwistle", 58, 71],
["Jason", "Blashaw", 49, 80],
["Louise","Smith", 81, 67],
["Sara", "Acton", 37, 66],
["Donna", "Alexander", 84, 86],
["Michael", "Mitchelle", 65, 55],
["Anthony", "Lewis", 48, 50],
["Sharon", "Grant", 53, 70],
["Peter", "Hughes", 82, 90],
["Deborah", "Biddle", 51, 47],
["Dawn", "Doens", 35, 44],
["William", "Dennis", 72, 73],
["Selim", "Biddle", 52, 67],
["Ian", "Nadeem", 40, 36],
["Jenny", "Thomson", 56, 43],
["Rowena", "Moore", 50, 77],
["Jane", "Murphy", 44, 48]]

message = [
"student failed both tests",
"student failed one test",
"student passed both with distinction",
"student passed both tests"]

for student in studentTestScores:
    first = student[0]
    last = student[1]
    english = student[2]
    maths = student[3]

    print(first, last, ": ")
    if (english < 40 and maths < 50):      # student failed both
        messageIndex = 0
    elif (english < 40 or maths < 50):     # student failed one
        messageIndex = 1
    elif (english >= 80 and maths >= 85):   # student passed both with distinction
        messageIndex = 2
    else:
         messageIndex = 3
         
    print(message[messageIndex])
    
    
