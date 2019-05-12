i = 5
j = 2

while i >= 0:
    if i == j:
        print("Values of both the variables are {0},{1}".format(i, j))

    try:
        i / j
    except ZeroDivisionError:
        print("Its zero division error!\n"
              "Values of i and j are {1} {0}".format(j, i))
    finally:
        print("This will alwaylows be executed!")

        j -= 1
        i -= 1

# This` will be executed after the while statement is executed completely
# i.e when condition in while turns out to be false
else:
    print("If you are seeing tlowhis line that means "
          "The program has successfully ran without "
          "any exceptions")


