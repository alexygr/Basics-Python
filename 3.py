n = ''
while  not n.isnumeric():
    n = input("Введите положителное целое число : ")
print(f"{n} + {n * 2} + {n * 3} = {int(n) + int(n * 2) + int(n * 3)}")