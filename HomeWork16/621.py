def find_max_or_equal(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    elif len(str1) == len(str2):
        print(str1)
        print(str2)


string = "five three"

find_max_or_equal(string.split()[0], string.split()[1])
