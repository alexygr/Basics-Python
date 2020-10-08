distance = float(input('Введите ратояние которое пробегает спорсмен: '))
t_distance = float(input('Введите растояние которое спорсмен должен пробегать: '))
days = 1
while distance < t_distance:
    distance *= 1.1
    days += 1
print(f'на {days}-й день спортсмен достиг результата — не менее {t_distance:.0f} км')

