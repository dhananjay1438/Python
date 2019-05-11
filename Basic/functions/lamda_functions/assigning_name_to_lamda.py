# assigning name to lambda


func1 = lambda x : x**2

print(func1(2))

func2 = lambda x : x*'hello '

print(func2(10))

func3 = lambda: print("hello")

print(func3())

func1_type = type(func1)
func3_type = type(func3)

print(f"Type of func1 is {func1_type} \n And Type of func3 is {func3_type}")

print("Type of func1 is {func1_type} \n And Type of func3 is {func3_type}".format(func1_type=func1_type,\
                                                                                  func3_type=func3_type))