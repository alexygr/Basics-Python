my_list = [7, 5, 3, 3, 2]
while True:
    n = input("Input number from 0 - 9: ")
    if n == 'q':
        break
    while True:
        if not n.isnumeric():
            n = input("It must have be number from 0 - 9: ")
        elif int(n) < 0 or int(n) > 9:
            n = input("It must have be number from 0 - 9: ")
        else:
            break
    n = int(n)

    i = 0
    while i < len(my_list):
        if n <= my_list[i]:
            i += 1
        else:
            break
    my_list.insert(i, float(n))

    print(my_list, "\nFor quit type 'q'")
