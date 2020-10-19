def my_func(x, y):
    answer = x
    try:
        x, y = float(x), int(y)
        if x > 0 > y:
            y -= y
            for i in range(y):
                answer = answer * x
            return 1/answer
        else:
            return "'x' - действительное положительное число, 'y' - целое отрицательное."
    except ValueError:
        return "Програма работает только с числами.\n" \
               "'x' - действительное положительное число, 'y' - целое отрицательное."


print(my_func(23, -2))
