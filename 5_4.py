def translate(num):
    my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    return my_dict[num]


ru_f = open("text_4r.txt", "w", encoding="utf-8")
with open("text_4.txt", encoding="utf-8") as ang_f:
    for line in ang_f:
        world = line.split(" - ")
        world[0] = translate(world[0])
        ru_f.write(f"{world[0]} - {world[1]}")
ru_f.close()
