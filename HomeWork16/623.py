def min_max(num_list):
    if not num_list:
        return None

    min_num = max_num = num_list[0]

    for i in num_list:
        if i < min_num:
            min_num = i
        elif i > max_num:
            max_num = i

    return (min_num, max_num)

numbers = [61, 9, -5, 23, 15, 44, 31, 10, -14, 7, 8]

print(min_max(numbers)) # на вебсайті написано что вихідні дані (-14, 44)
