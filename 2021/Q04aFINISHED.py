# Q04(a)

import random

# Get input
product_name = input("Enter a product name: ")



# Generate a random number between 10 and 30 inclusive
num = random.randint(10, 30)



# Generate the product code - first three letters of product name and the random number
product_code = product_name[:3] + str(num)



# Display the product code and the product name
print(product_code)


