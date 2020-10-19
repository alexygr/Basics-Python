def int_func(string=""):
    for i in range(len(string)):
        if ord(string[i]) < 97 or ord(string[i]) > 122:
            return ""
    return string.title() + " "


# print(int_func(input("Ведите слово маленкими латинскими буквами")))
expr = input("Ведите предложение маленкими латинскими буквами").split()
for el in expr:
    print(int_func(el), end="")
