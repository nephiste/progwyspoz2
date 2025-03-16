class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        return Matrix(self.a + other.a, self.b + other.b, self.c + other.c, self.d)

    def __mul__(self, other):
        return Matrix(
            self.a * other.a + self.b * other.c,
            self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c,
            self.c * other.b + self.d * other.d
        )

    def __str__(self):
        return (f'''[{self.a},{self.b};
 {self.c},{self.d}]''')

    def __repr__(self):
        return f'({self.a},{self.b},{self.c},{self.d})'

ma1 = Matrix(2, 3, 5, 7)
ma2 = Matrix(4, 5, 6, 8)
print(repr(ma1))
print(ma1)
print(ma1 + ma2)
print(ma1 * ma2)
