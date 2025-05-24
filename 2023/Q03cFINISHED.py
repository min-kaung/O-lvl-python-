# Q03c

# -----------------------------------------------------
# Write your code below this line
base = int(input("Enter base value (0 to exit): "))

while base != 0:
    
    exponent = int(input("Enter value for exponent: "))
    if exponent < 0:
        print("Error!, exponent cannot be negative")
    else:
        answer = 1
        count = 0
        
    while count < exponent:
        answer =  answer * base
        count += 1
    
    print("base -", answer, ", exponent -", exponent, ", answer -", answer)
    base = int(input("Enter base value (0 to exit): "))