max = 0
number = 1
while number < 10:
    number = int(input('Введите многозначное число : '))
while number > 0:
    if number % 10 > max:
        max = number % 10
    number //= 10
print(max)
