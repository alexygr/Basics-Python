class ZerroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    x = input("Ведите делимое:  ")
    try:
        x = float(x)
    except ValueError:
        print("Это должно быть число")
        break

    y = input("Введите делитель")
    try:
        y = float(y)
        if y == 0:
            raise ZerroDiv("Нельзя делить на ноль")
    except ValueError:
        print("Это должно быть число")
        break
    except ZerroDiv as err:
        print(err)
        break
    else:
        print(f"{x/y}")
        break

