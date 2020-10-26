moon = open("text_3.txt", "r", encoding="utf-8")
data = [line.split() for line in moon]
evrg = 0
print("Cотрудники с зарплатой меньше 20000")
for el in data:
    if float(el[1]) < 20000:
        print(f"{el[0]}")
    evrg += float(el[1])

print(f"Средняя зарплата - {evrg/len(data)}")
print(f"всего сотрудников {len(data)}")
moon.close()
