string = input("Enter a string")
subString = input("Enter sub string to find")

isTrue = subString in string

if isTrue:
    print("Substring is present in the string!")
else:
    print("Substring is not present in the string!")
    