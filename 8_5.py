class ComplexNumber:
    def __init__(self, a, j):
        self.a = a
        self.j = j

    def __mul__(self, other):
        a = self.a * other.a - self.j * other.j
        j = self.a * other.j + self.j * other.a
        return complex(a, j)

    def __add__(self, other):
        a = self.a + other.a
        j = self.j + other.j
        return complex(a, j)

    def __str__(self):
        return f"{complex(self.a, self.j)}"


num1 = 3 - 4j
num2 = 2 + 1j
print(f"({(3 * 2 - -4 * 1)}{(3 * 1 + 2 * -4)}j)")
print(num1 * num2)
n1 = ComplexNumber(3, -4)
n2 = ComplexNumber(2, 1)
print(f"{n1} * {n2} =  {n1 * n2}")
print(f"{n1} + {n2} =  {n1 + n2}")
