def print_even_numbers(num):
    even_numbers = [i for i in num if i % 2 == 0]
    print(' '.join(map(str, even_numbers)))


inp = [32, 4, 7, 9, 11, 13, 15, 8]

print_even_numbers(inp)
