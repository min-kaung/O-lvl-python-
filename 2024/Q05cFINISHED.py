# Q05c

INPUT_FILE = "Sales.txt"    # Output file name
COMMA = ","                 # Use as a constant

subTotal = 0        # Subtotal for each line
grandTotal = 0      # Running total

# Complete the code to open the file for reading
theFile = open(INPUT_FILE, "r")

# Complete the code to read each line of the input file
for line in theFile:

    # Complete the code to split the line into a set of five strings
    stringSales = line.split(COMMA)
    
    subTotal = 0   
    # Add code to sum up each value in the set of five strings
    for value in stringSales:
        subTotal += int(value)

    # Add code to display the subtotal for the line
    print("Sub total:", subTotal)

    # Add code to calculate the running total
    grandTotal += subTotal

# Add code to display the total of all lines in the file
print("Grand Total:", grandTotal)

# Complete the code to close the opened file
theFile.close()

