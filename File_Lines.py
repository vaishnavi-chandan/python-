# Read all lines from a file into a list.Print the total no. of lines
# and display the  2nd and 4th line.
with open("Random.txt", "r") as f:
    lines = f.readlines()
    print("Total number of lines in the file:", len(lines))
    if len(lines) >= 4:
        print("The 2nd line is:", lines[1].strip())
        print("The 4th line is:", lines[3].strip())
    else:
        print("The file does not have enough lines to display the 2nd and 4th lines.")