str = "Hello World"

index = 0
for i in str:
    print(index, i, end=", ")
    index += 1

# Better way to do this

print("\nBetter Way to do this")

for i in range(len(str)):
    print(i, str[i], end=", ")

print("\nAnd much better way to to this is:")

for i, c in enumerate(str):
    print(i, c, end=", ")