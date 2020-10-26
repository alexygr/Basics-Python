import json
dict_comp = {}
with open("text_7.txt", "r", encoding="utf-8") as file_obj:
    for line in file_obj:
        my_str = line.split()
        dict_temp = {my_str[0]: int(my_str[2]) - int(my_str[3])}
        dict_comp.update(dict_temp)
print(dict_comp)
my_sum = 0
count = 0
for val in dict_comp.values():
    if val > 0:
        my_sum += val
        count += 1
dict_avr = {"average_profit": int(my_sum/count)}
data = [dict_comp, dict_avr]
print(data)
with open("text7_1.json", "w", encoding="utf-8") as file_obj:
    json.dump(data, file_obj)
json_obj = json.dumps(data)
print(json_obj)
