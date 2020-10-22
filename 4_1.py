from sys import argv
try:
    print(f"Заработная плата выработка в часах-{argv[1]} * ставка в час-{argv[2]} + премия-{argv[3]}\n")
    print(f"{(float(argv[1]) * float(argv[2]) + float(argv[3])):.02f}")
except ValueError:
    print("Неверный ввод")
except IndexError:
    print("Ошибка. Введите - выработка в часах * ставка в час + премия")
