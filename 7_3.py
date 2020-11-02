class Cell:
    def __init__(self, cell=1):
        self.cell = cell

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell((self.cell - other.cell) if self.cell-other.cell > 0 else f"В клетке должна быть хотя бы одна ячейка")

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell((self.cell // other.cell) if self.cell//other.cell > 0 else f"В клетке должна быть хотя бы одна ячейка")

    def __str__(self):
        return f"{self.cell}"

    def make_order(self, x):
        string = ""
        cell = self.cell
        for i in range(cell//x):
            string += "*" * x + "\n"
        string += "*" * int(cell % x)
        return  string


s1 = Cell(16)
s2 = Cell(15)
print(s2/s1)
print(f"{s1+s2}")
print(f"{s2 - s1}")
s3 = s1 + s2
print(s3.make_order(5))

