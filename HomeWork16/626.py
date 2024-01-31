def stars(count):
    for num in count.split(","):
        for i in range(int(num)):
            print("*", end="")


user_input = input()

stars(user_input)
