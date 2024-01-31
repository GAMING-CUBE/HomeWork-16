def calculate(list_):
    product = 1
    for element in list_:
        product *= element
    return product


inp = [1, 10, 4, 8, 11, 5, 2]

print(calculate(inp))
