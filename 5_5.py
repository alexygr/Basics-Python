while True:
    try:
        my_list = input("Введите числа разденыые пробелами").split()
        my_list = list(map(float, my_list))
        break
    except ValueError:
        print("Error")

file_obj = open("test2.txt", "w+", encoding="utf-8")
for el in my_list:
    file_obj.writelines(f"{str(el)} ")
file_obj.seek(0)
my_list = file_obj.read().split()
my_list = list(map(float, my_list))
print(sum(my_list))
file_obj.close()

