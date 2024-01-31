def calculate(num1, num2, calculation):
    if calculation == "+":
        print(str(num1 + num2))
    elif calculation == "-":
        print(num1 - num2)
    elif calculation == "*":
        print(num1 * num2)
    elif calculation == "/":
        print(num1 / num2)
    else:
        print("Unknown operation")


first_num = int(input())
second_num = int(input())
calculation_method = str(input())

calculate(first_num, second_num, calculation_method)
