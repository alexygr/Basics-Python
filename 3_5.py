def my_func():
    result = 0
    while True:
        my_str = input("Введите числа разделённые пробелами: ").split()
        for i in range(len(my_str)):
            try:
                result += int(my_str[i])
            except ValueError:
                if my_str[i] == 'q':
                    return print(f"Сумма чисел = {result}")
                else:
                    print("Для выхода введите 'q'")
        print(f"Сумма чисел = {result}")


my_func()
