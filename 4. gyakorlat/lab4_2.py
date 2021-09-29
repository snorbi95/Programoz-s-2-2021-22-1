class BankAccount:

    def __init__(self, p1):
        self.money = p1

    def deposit(self, p1):
        self.money += p1
        print(self)

    def withdraw(self, p1):
        self.money -= p1
        print(self)

    def __str__(self):
        return f'Az egyenleg: {self.money}'

# b1 = BankAccount(500)
# b1.deposit(500)
# b1.withdraw(1000)

class MinBankAccount(BankAccount):

    def __init__(self, money, min_value):
        super().__init__(money)
        self.min_value = min_value

    def withdraw(self, p1):
        if self.money - p1 < self.min_value:
            return 'A tranzakcio nem vegrehajthato'
        else:
            super().withdraw(p1)

min_bank = MinBankAccount(5000,500)
print(min_bank.withdraw(4500))