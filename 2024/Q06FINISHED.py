# Q06

tblWords = [["apple", "banana"],
              ["wrist", "leg"],
              ["blue", "yellow"],
              ["speaker", "keyboard"],
              ["lavender", "tulip"],
              ["pencil", "chalk"],
              ["apartment", "house"],
              ["bottom", "top"],
              ["snow", "fog"],
              ["beach", "mountain"],
              ["", ""]]

word1 = "newspaper"
word2 = "book"

# ----------------------------------------------
# Write your code below this line
tblWords[-1][0] = word1
tblWords[-1][1] = word2

count = 1
for item in tblWords:
    print(count, item[0], item[1])
    
    if len(item[0]) > len(item[1]):
        print("\t", item[0])
    else:
        print("\t", item[1])
    
    if item[0] > item[1]:
        print("\t", item[1], item[0])
    count += 1