char = input("Enter a character: ")
if len(char) > 1:
    print("Enter a single character")
else:
    print("The ASCII value of the character is: ", ord(char))