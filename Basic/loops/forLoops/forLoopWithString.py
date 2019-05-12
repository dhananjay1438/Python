string = "Hello World"

index = 0
for i in string:
    print(index, i, end=", ")
    index += 1

# Better way to do this

print("\nBetter Way to do this")

for i in range(len(string)):
    print(i, string[i], end=", ")

print("\nAnd much better way to to this is:")

for i, c in enumerate(string):
    print(i, c, end=", ")
