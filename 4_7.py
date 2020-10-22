def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result


number = int(input("input some number"))
fact_list = [el for el in fact(number)]
print(fact_list)
