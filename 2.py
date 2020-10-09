time = int(input('Введите время в секундах : '))
print(f'{(time // 60 // 60):02d}:{(time // 60 % 60):02d}:{(time % 60):02d}')
