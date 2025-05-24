#Q02bii

# Weight in grams for each portion of chips
PORTION_ADULT = 85
PORTION_CHILD = 70

# Get the total weight of chips in stock, in kilograms
inStock = int (input ("Enter the weight of chips available in kilograms: "))
inStock = 1000 * inStock

# Get the number of adults and the number of children
numAdults = int (input ("Enter the number of adult tickets sold: "))
numChildren = int (input ("Enter the number of child tickets sold: "))

# Calculate weight of adult and child portions
weightAdult = numAdults * PORTION_ADULT
weightChild = numChildren * PORTION_CHILD

# Calculate total weight required
requiredWeight = weightAdult + weightChild

# Tell staff the weight available and the weight required
print ("Available: ", inStock, "Required: ", requiredWeight)

# Check if available weight is enough for the dinner
if (requiredWeight <= inStock):
    print ("Stocks available")
else:
    # Tell the staff how much more to order in kilograms
    weightNeed = (requiredWeight - inStock) / 1000
    print ("Order", weightNeed, "kilograms.")

