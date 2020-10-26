moon = open("test.txt", "w+", encoding="utf-8")
while True:
    my_line = input("Write some text, for exit press 'Enter': ")
    if not my_line:
        break
    moon.write(my_line+"\n")
moon.close()