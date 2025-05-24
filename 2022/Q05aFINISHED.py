# Q05(a)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; # Valid uppercase letters in the alphabet
digit = "0123456789"; # Valid digits

passwordFile = open("passwords.txt", "r") # Open the file password.txt to read

# Add your code here
incorrectPasswords = 0
passwords = passwordFile.readlines()

for password in passwords:
    correct = False
    if password[0] in alphabet:
        for cha in password:
            if cha in digit:
                correct = True
    
    if not correct:
        print("Invalid -", password)
        incorrectPasswords += 1
        
print("numbers of incorrect passwords", incorrectPasswords)
passwordFile.close()