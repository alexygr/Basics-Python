my_list = ['text', True, 23, 0.4, None, b"text", [2, 3],
           bytearray(b"text"), (True, False), {2, 3, 4}, {1: 'one', 2: 'two'}]
for el in my_list:
    print(type(el))
    print(el)
