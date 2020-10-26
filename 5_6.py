def convrt(text=""):
    i = text.find(":")
    key = text[:i]
    value = list(text[i+1:])
    for n in range(len(value)):
        if ord(value[n]) < 48 or ord(value[n]) > 57:
            value[n] = " "
    return key, sum(map(int, "".join(value).split()))


data = {}
with open("text_6.txt", "r", encoding="utf-8") as file_obj:
    for line in file_obj:
        temp_dict = {(convrt(line))}
        data.update(temp_dict)
print(data)
