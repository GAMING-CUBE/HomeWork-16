def paste_string_in_the_middle(main_string, paste_string):
    if len(paste_string) >= 2:
        start = main_string[0]
        end = main_string[-1]
        paste_string = paste_string.join(main_string[1:-1])
        return start + paste_string + end
    else:
        return main_string


string = ["[] Python", "<<>> HTML", "qwerty 123"]

for i in string:
    parts = i.split()
    print(paste_string_in_the_middle(parts[0], parts[1]))
