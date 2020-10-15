my_list = input("Enter some text: ")
my_list = list(my_list)
print(my_list)
list_lenth = len(my_list)-len(my_list)%2
i = 0
while i < list_lenth:
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
print(my_list)
