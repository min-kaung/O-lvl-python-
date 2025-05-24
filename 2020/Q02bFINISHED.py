#	Q02b

#	Set initial values of variables
length = 0
width = 0

# 	Request input
length = int(input("Enter the length of the building (in metres): "))
width = int(input("Enter the width of the building (in metres): "))

# 	Calculate number of panels needed
panels = (2 * (length + width) - 4) / 1

# 	Print out number of panels needed
print("Minimum number of full panels needed", panels)