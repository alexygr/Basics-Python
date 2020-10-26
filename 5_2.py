moon = open("test.txt", "r", encoding="utf-8")
i = 0
for line in moon:
    i += 1
    print(f"В стоке {i} - {len(line.split())} слова.")
print(f"Всего строк в файле {moon.name} - {i}.")
moon.close()
