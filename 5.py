proceeds = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))
if proceeds > costs:
    print(f'Вы работаете с прибылью , рентабельность {proceeds / costs:.2f}')
    staff = int(input('Слолько сотрудников у вас работает?'))
    print(f'Прибыль на сотрудника {(proceeds-costs)/staff:.2f}')
elif proceeds < costs:
    print("Вы работаете в убыток")
else:
    print('Вы остаётесь при своём')
