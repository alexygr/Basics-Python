my_string = input("Write some sentence")
my_list = my_string.split(" ")
i = 1
for el in my_list:
    print(f"{i}. {el}")
    i += 1