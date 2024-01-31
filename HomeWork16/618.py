def is_at_the_start(string):
    if not string[0:2] == "Is":
        print("Is", string)
    else:
        print(string)


a = "list"
b = "Is empty"

is_at_the_start(a)
is_at_the_start(b)
