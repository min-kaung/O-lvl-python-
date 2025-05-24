#   Q6

#   Structure of sales record is
#   StaffID, First name, Last name, January sales, February sales,
#   March sales, April sales, May sales, June sales

staffSales = [
["101TGY" , "George" , "Taylor" , 6009 , 5262 , 3745 , 7075 , 1943 , 4432],
["103FCY" , "Fehlix" , "Chayne" , 8717 , 2521 , 5777 , 6189 , 5089 , 6957],
["102SBY" , "Sumren" , "Bergen" , 5012 , 1063 , 7937 , 9560 , 1115 , 5499],
["104SBK" , "Samira" , "Beckle" , 1140 , 9206 , 3898 , 8544 , 5937 , 8705],
["105NBT" , "Nellie" , "Bogart" , 3017 , 3342 , 5939 , 2479 , 3374 , 2297],
["106CGT" , "Cheryl" , "Grouth" , 9620 , 7160 , 5113 , 4803 , 5492 , 2195],
["107DGT" , "Danuta" , "Graunt" , 1583 , 7450 , 1026 , 7463 , 2390 , 6509],
["108JDN" , "Jaiden" , "Deckle" , 4064 , 4978 , 2984 , 3159 , 1464 , 4858],
["109JCK" , "Jimran" , "Caliks" , 6253 , 7962 , 2732 , 7504 , 2771 , 5193],
["110DDN" , "Deynar" , "Derran" , 6305 , 8817 , 5200 , 3647 , 3365 , 1256]]


#--------------------------------------------------------------------------
#   Write your code below this line
total = 0
highest = -999
highest_name = ""
second = -999
second_name = ""

for staff in staffSales:
    totalEach = 0
    
    # calculating total sales of each staff
    for i in range(3, len(staffSales)-1):
        totalEach += staff[i]
    
    print("Total Sales made by", staff[1], staff[2], "-" ,totalEach)
    
    # calculating total sales made by whole team
    total += totalEach
    
    # selecting highest and second highest 
    if totalEach > highest:
        second = highest
        second_name = highest_name

        highest = totalEach
        highest_name = staff[1] + " " + staff[2]
    elif totalEach > second:
        second = totalEach
        second_name = staff[1] + " " + staff[2]
    
print("\nTotal sales made by the whole team: ", total)
print("\nHighest total sales:", highest, "by -", highest_name)
print("Second Highest total sales:", second, "by -", second_name)