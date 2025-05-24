# Q03a

#	Open the file and input data
myfile = open("Email.txt","r")

#	Open output file
outfile = open("Error.txt", "w")

#	Find errors and write to output file
for line in myfile:
    if "@" not in line:
        outfile.write(line + "\n")

#	Close files
myfile.close()
outfile.close()