def find_month(month_num):
    if 1 <= month_num <= 12:
        if 3 <= month_num <= 5:
            return "spring"
        elif 6 <= month_num <= 8:
            return "summer"
        elif 9 <= month_num <= 11:
            return "autumn"
        else:
            return "winter"
    else:
        return "unknown"


months = [6, 2, 9, 3, 15]

for i in months:
    print(find_month(i))
