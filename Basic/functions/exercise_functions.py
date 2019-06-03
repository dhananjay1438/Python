import string


def up_low(text):
    i = 0
    lower_chars = 0
    upper_chars = 0
    lower_text = text.lower()
    while i <= len(text) - 1:
        if 'z' >= text[i].lower() >= 'a':
            if text[i] == lower_text[i]:
                lower_chars += 1
            else:
                upper_chars += 1

        i += 1
    print(f"Lower letters = {lower_chars} \n"
          f"Upper letters = {upper_chars}")


up_low("HeDFll Sd")
up_low("Hello Mr. Rogers, how are you this fine Tuesday?")


def unique_list(nums):
    new_set = set()
    for num in nums:
        new_set.add(num)
    print(new_set)
    print(type(new_set))

    my_temp_list = list(new_set)

    print(my_temp_list)
    print(type(my_temp_list))


unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])


def multiply(*args):
    multiplication = 1
    for arg in args:
        multiplication *= arg
    return multiplication


print(multiply(1, 2, 4, -2))


def palindrome(string):
    if string[::-1] == string:
        print("String is palindrome")
    else:
        print("String is not palindrome")


palindrome("nurses")
palindrome("madam")


def pangram(text, alphabets=string.ascii_lowercase):
    text_set = set(text.lower().replace(" ", ""))
    alphabets_set = set(alphabets)
    if text_set == alphabets_set:
        print("Pangram")
    else:
        print("Not pangram")


pangram("The quick brown fox jumps over the lazy dog")
pangram("abcdefghijklmnopqurstuvwxyADSF")

