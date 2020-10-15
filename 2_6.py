from typing import Dict, Any, Union, Tuple

count = 3
analiz = {}

stuf = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]
commodity = dict(название="клавиатура", цена=500, количество=4, ед="шт")
count += 1
set_commdity = (count, commodity)
stuf.append(set_commdity)

i = 0
for key in stuf[0][1].keys():
    name = []
    for i in range(len(stuf)):
        name.append(stuf[i][1].get(key))
    tmpdict = {key: name}
    analiz.update(tmpdict)

print(analiz)


