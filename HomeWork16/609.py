def calculate(num1, num2):
    print(int(num1) + int(num2))

numbers = input()
numbers = list(numbers.split())

calculate(numbers[0], numbers[1])