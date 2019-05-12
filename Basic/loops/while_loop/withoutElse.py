
i = 10
j = 0
a = 0
while a <= 5:
    a += 1
    try:
        i / j
    except ZeroDivisionError:
        print("Zero division error")


else:
    print("Let's see if this runs!")