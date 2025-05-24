# Q03

#  Initialise variables
total = 0
price = 0


#  Print prompt and take number of textbooks required
numberBooks = int(input("Enter the number of books required:"))

#  Generate and display the price per textbook and the total cost
if 1 <= numberBooks <= 5:
    price = 20
elif numberBooks <= 9:
    price = 15
elif numberBooks >= 10:
    price = 12
else:
    price("invalid quantity")

cost = price * numberBooks

if cost > 0:
    price("price per book is ", price)
    print("total cost £", cost)