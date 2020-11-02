from itertools import zip_longest


class Matrix:
    def __init__(self, m):
        self.m = m

    def __str__(self):
        my_str = ""
        for i in self.m:
            for j in i:
                my_str += f"{j}\t"
            my_str += "\n"
        return my_str

    def __add__(self, other):
        m = []
        for i1, i2 in zip_longest(self.m, other.m, fillvalue=0):
            if i1 == 0:
                i1 = [0 for _ in i2]
            elif i2 == 0:
                i2 = [0 for _ in i1]
            m_temp = [j1 + j2 for j1, j2 in zip_longest(i1, i2, fillvalue=0)]
            m.append(m_temp)
        return Matrix(m)


m1 = Matrix([[1, 2], [1, 2]])
m2 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
m3 = m1 + m2
print(m3)
print(m3+m1)
