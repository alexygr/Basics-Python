def sub_f(arg_1, arg_2):
    if arg_1.isnumeric() and arg_2.isdigit():
        if not int(arg_2) == 0:
            return float(arg_1) / float(arg_2)
        else:
            return "Нельзя делить на ноль"
    else:
        return "Это должны быть числа"


num_1 = input("Введите делимое: ")
num_2 = input("Ведите делитель: ")
print(sub_f(num_1, num_2))
