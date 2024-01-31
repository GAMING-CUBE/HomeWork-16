def transform_letters(input_str, n, m):
    if input_str[:m].count('A') + input_str[:m].count('a') >= n:
        return input_str.upper()
    else:
        return input_str


input_str = input()
n, m = map(int, input().split())

result = transform_letters(input_str, n, m)
print(result)
