class Calkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def truediv(self):
        return self.a / self.b


calkulator = Calkulator(40, 15)
print(f'сложение {calkulator.add()}')
print(f'вычитание {calkulator.sub()}')
print(f'умножение {calkulator.mul()}')
print(f'деление {round(calkulator.truediv(), 2)}')
