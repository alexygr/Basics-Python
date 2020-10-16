count = 0
analize = {}
stuf = []
while True:

    print("1 - Добавить товар\n"
          "2 - Вывести анализ\n"
          "3 - Выйти из програмы")

    switch = input(": = >")
    if switch == '1':
        name = input("Введите имя товара")
        price = float(input("Введите цену товара"))
        quantity = int(input("Введите количество товара"))
        unit = input("Введите единицу измерения")

        commodity = {"название": name, "цена": price, "количество": quantity, "eд": unit}
        count += 1
        set_commodity = (count, commodity)
        stuf.append(set_commodity)
        for el in stuf:
            print(el)
    elif switch == '2':
        for key in stuf[0][1].keys():
            name = []
            for i in range(len(stuf)):
                name.append(stuf[i][1].get(key))
            tmpdict = {key: name}
            analize.update(tmpdict)

        for key, value in analize.items():
            print(f"{key}: {value}")

    elif switch == '3':
        break
    else:
        print("Неверный ввод")
