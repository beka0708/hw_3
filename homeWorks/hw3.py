print('работать тут')


class _Bank:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        while 1:
            card = int(input('1)Узнать ваш баланс \n2)Пополнить баланс '))
            if card == 1:
                print(f'Ваш баланс {self._balance}')
                break
            elif card == 2:
                top_up = int(input('Сколько хотите добавить? '))
                print(f'Теперь ваш баланс составляет {self._balance + int(top_up)}')
                break
            else:
                print("Введите правильный номер!!!")

    def _kill(self):
        print(f'Ваш счет обнуляется')
        self._balance = self._balance - self._balance
        return self._balance

    def __str__(self):
        return f' name {self._name}, balance {self._balance}'

    def __jackpot(self):
        print(self._balance * 10)

    @property
    def jackpot(self):
        return self.__jackpot

    def copy(self, other):
        print(f'{self._balance + other._balance} and {other._balance} ')


account1 = _Bank('Beka', 2000)
account2 = _Bank('Tima', 1000)
account1.moneyX()
print(account1._kill())
print(account1.__str__())
# print(account1.jackpot)
# print(dir(_Bank))
# account1._Bank__jackpot()
account1.copy(account2)


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
