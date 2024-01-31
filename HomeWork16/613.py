def find_num(num1, num2):
    if num1 == num2:
        print("equal")
    else:
        print(max(num1, num2))


inp = input()
inp = list(inp.split())

find_num(inp[0], inp[1])
