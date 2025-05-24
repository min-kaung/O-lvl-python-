# Q05c

tbl_tuna = [["Yellowfin",105,15,3],
            ["Albacore",90,15,5],
            ["Skipjack",50,3,4],
            ["Bigeye",105,25,4],
            ["Atlantic Bonito",50,4,2],
            ["Northern Bluefin",190,120,11],
            ["Southern Bluefin",190,120,11],
            ["Tongol",90,20,4]]


# ----------------------------------------------
# Write your code below this line
number_prefix = 100

myFile = open("TunaData.txt", "w")
for tuna in tbl_tuna:
    number_prefix += 1

    string = str(number_prefix) + "," + tuna[0]
    for i in range(1, len(tuna)):
        string += "," + str(tuna[i])

    myFile.write(string + "\n")

myFile.close()