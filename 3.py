#x = 0
#sum = 0
while x < 1 or x > 9:
    x = int(input('Введите число от 1 до 9 : '))
while x > 0:
    sum += x
    x -= 1
print (sum)
