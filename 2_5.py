str = [7, 5, 3, 3, 2]
while True:
    n = input("Input number from 0 - 9: ")
    if n == 'q': break
    while True:
        if not n.isnumeric():
            n = input("It must have be number from 0 - 9: ")
        elif int(n) < 0 or int(n) > 9:
            n = input("It must have be number from 0 - 9: ")
        else:
            break
    n = int(n)
    """str.append(n)
    str.sort(reverse=True)"""
    i = 0
    while i < len(str):
        if n > str[i]:
            str.insert(i, n)
            break
        if i == len(str)-1:
            str.append(n)
            break
        i += 1

    print(str, "\nFor quit type 'q'")
