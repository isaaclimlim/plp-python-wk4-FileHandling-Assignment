
# How to read the file
file1 = open("praco.txt", "r")
print(file1.read())


# How to write the file
file1 = open("praco.txt", "w")
file1.write("It is creative to use python for automation.")

# How to handle errors
try:
    file1 = input("Please enter the name of the file you want to: ")
    file1 = open(file1, "r")
    print(file1.readlines())

except FileNotFoundError as error:
    print("The file does not exist.")






