# Q06

tbl_breed = ["Red Chittagong", "Sussex", "Dexter", "Abondance",
             "Sahiwal", "Vorderwald", "Ayrshire", "Jersey",
             "Randall", "Alderney", "Carora", "Gloucester"]
tbl_rating = [1, 2, 3, 2, 3, 1, 2, 1, 2, 1, 3, 2]
tbl_count = [6, 3, 8, 7, 6, 4, 3, 7, 3, 3, 4, 7]
tbl_volume = [7.5, 5.7, 11.4, 11.4,
              22.0, 15.2, 21.0, 18.3,
              19.0, 9.0, 23.1, 16.0]
tbl_dailyVolume = []

# ----------------------------------------------
# Write your code below this line
total = 0
highest_rating = 99
highest_vol = -99
best_index = 0

print("Fields are: Breed, Rating, Volume (cow), Count, Volume (day)")

for i in range(len(tbl_breed)):
    # calculating daily volume for each breed
    dailyVol = 0
    dailyVol = tbl_count[i] * tbl_volume[i]
    tbl_dailyVolume.append(tbl_count[i] * tbl_volume[i])

    # printing data for each breed
    print(tbl_breed[i], tbl_rating[i], tbl_volume[i], tbl_count[i], tbl_dailyVolume[i])
    
    # calculating total volume of milk by the herd
    total += dailyVol
    
    if tbl_rating[i] <= tbl_rating[best_index] and tbl_volume[i] > tbl_volume[best_index]:
        best_index = i
    

print("Total:", total, "litres")
print("Recommended breed:", tbl_breed[best_index], "rating:", tbl_rating[best_index], "volume:", tbl_volume[best_index])