def create_and_print_dict(n):
    dictionary = {i: i**2 for i in range(1, n+1)}
    print(dictionary)


inp = 10

create_and_print_dict(inp)
