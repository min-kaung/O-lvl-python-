# Q02a

# Initialise variables
username = "bard423"
password = "nX2934"

# Print prompts, take and check input from user
access = False

while not access:
    input_username = input("Enter username: ")
    input_pw = input("Enter password: ")
    if input_username == username:
        if input_pw == password:
            print("Access granted! Welcome.")
            access = True
    else:
        print("Error!")


