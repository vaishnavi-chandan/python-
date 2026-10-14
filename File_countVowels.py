# Program to read a file and count the number of vowels in it.
name = input("Enter the file name: ")
with open(name, "r") as f:
    data = f.read()
    vowels = "aeiouAEIOU"
    count = 0
    for char in vowels:
        count += data.count(char)
    print("The number of vowels:", count)

