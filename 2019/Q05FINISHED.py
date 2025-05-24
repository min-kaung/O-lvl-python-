#Q05FINISHED

libraryRecord =  [
["105MS" , "Marcus" , "Smith" , 25 ],
["103AZ" , "Anthony" , "Zarrent" , 5 ],
["108MW" , "Matt" , "White" , 12 ],
["112DB" , "Denise" , "Bilton" , 58 ],
["124MK" , "Malcolm" , "Kelly" , 26 ],
["116UK" , "Uzere" , "Kevill" , 29 ],
["127AL" , "Abduraheim" , "Leahy" , 94 ],
["124LS" , "Laura" , "Sampras" , 50 ],
["121AP" , "Azra" , "Potter" , 61 ],
["115AC" , "Anthony" , "Calik" , 10 ],
["117PI" , "Pablo" , "Iilyas" , 49 ],
["113MM" , "Mark" , "Montgomerie" , 68 ],
["130FH" , "Felicity" , "Heath" , 11 ],
["132JA" , "Jill" , "Alexander" , 61 ],
["123SG" , "Sara" , "Grimstow" , 9 ],
["134KD" , "Kevin" , "Dawson" , 74 ],
["122AB" , "Andrew" , "Bertwistle" , 42 ],
["125JF" , "Jaide" , "Feehily" , 55 ],
["128JS" , "Justin" , "Slater" , 68 ],
["126CG" , "Colleen" , "Grohl" , 39 ]
]
# ----------------------------------------------
# Write your code below this line
gold = 0
silver = 0
bronze = 0
gold_name = ""
silver_name = ""
bronze_name = ""
gold_id = ""
silver_id = ""
bronze_id = ""

total = 0

# main loop
# counting total and average 
for student in libraryRecord:
    # calculating total number of books
    total += student[-1]
    
    # printing IDs of pupil who have read fewer than ten books
    if student[-1] < 10:
        print("ID of pupils who have fewer than ten book - ", student[0])

    # selecting awards
    if student[-1] > gold:
        bronze = silver
        bronze_name = silver_name
        bronze_id = silver_id

        silver = gold
        silver_name = gold_name
        silver_id = gold_id 
        
        gold = student[-1]
        gold_name = student[1] + " " + student[2]
        gold_id = student[0]
    elif student[-1] > silver:
        bronze = silver
        bronze_name = silver_name
        bronze_id = silver_id
        
        silver = student[-1]
        silver_name = student[1] + " "  + student[2]
        silver_id = student[0]
    elif student[-1] > bronze:
        bronze = student[-1]
        bronze_name = student[1] + " "  + student[2]
        bronze_id = student[0]
 
# calculating average number of books  
average = total // len(libraryRecord)

# printing total and average
print("\nTotal books: ", total)
print("Average books: ", average)

# printing award winners
print("\n  Gold winner: ID -", gold_id, "| Number of books -", gold,"| Name -", gold_name)
print("Silver winner: ID -", silver_id, "| Number of books -", silver,"| Name -", silver_name)
print("Bronze winner: ID -", bronze_id, "| Number of books -", bronze,"| Name -", bronze_name)