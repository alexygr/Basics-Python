Month_Dict = {1: "Ярварь",
              2: "Февраль",
              3: "Март",
              4: "Апрель",
              5: "Май",
              6: "Июнь",
              7: "Июль",
              8: "Август",
              9: "Сентябрь",
              10: "Октябрь",
              11: "Ноябрь",
              12: "Декабрь"}
Month_List = ["Ярварь", "Февраль", "Март", "Апрель", "Май", "Июнь",
              "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
Month_Number: int = 0
while Month_Number < 1 or Month_Number > 12:
    try:
        Month_Number = int(input('Введите число месяца: '))
    except:
        Month_Number = int(input('Введите число месяца: '))
print(f'{Month_Number} - {Month_Dict.get(Month_Number)}')
print(f'{Month_Number} - {Month_List[Month_Number-1]}')


