# Q04b

# ---------------------------------------------------------
# Write your code below this line
word = input("Enter a word: ")

if len(word) != 2 :
    print("Error! the word must be exactly two characters long")
else:
    whole_num = int(input("Enter a whole number: "))
    decimal_num = float(input("Enter a decimal number: "))

    key = str(whole_num) + word[-1] + word[0] + str(int(decimal_num))
    print(key)