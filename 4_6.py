from itertools import count, cycle, islice

my_list = [i for i in islice(count(3), 10)]
print(my_list)

for el in islice(cycle(my_list),30):
    print(el)
