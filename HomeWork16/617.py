def find_true_or_false(string1, string2, string3):
    if string1 == "список" or string1 == "кортеж" or string1 == "діапазон" or string1 == "рядок" or string1 == "байтів" or string1 == "байтовий масив" and string2 == "список" or string2 == "кортеж" or string2 == "діапазон" or string2 == "рядок" or string2 == "байтів" or string2 == "байтовий масив" and string3 == "список" or string3 == "кортеж" or string3 == "діапазон" or string3 == "рядок" or string3 == "байтів" or string3 == "байтовий масив":
        print("True")
    else:
        print("False")


string_input = list("Різні типи послідовностей (список, кортеж, словник)")
string_input = ''.join(string_input)
string_parts1 = string_input.split(" ")
string_input11 = string_parts1[3]
string_input12 = string_parts1[4]
string_input13 = string_parts1[5]
string_parts1 = string_input11.split("(")
string_parts2 = string_input12.split("(")
string_parts3 = string_input13.split("(")
string_input21 = string_parts1[1]
string_input22 = string_parts2[1]
string_input23 = string_parts3[1]
string_parts1 = string_input21.split(")")
string_input31 = string_parts1[0]
string_parts1 = string_input31.split(", ")
print(string_parts1)

#find_true_or_false(string_input2[0], string_input2[1], string_input2[2])
