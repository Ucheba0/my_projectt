class PersonalFinanceCalculator:
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.balance = 0

    def add_income(self, amount):
        if amount < 0:
            print("Ошибка: Сумма дохода не может быть отрицательной.")
        else:
            self.income += amount
            self.balance += amount

    def add_expense(self, amount):
        if amount < 0:
            print("Ошибка: Сумма расхода не может быть отрицательной.")
        else:
            self.expenses += amount
            self.balance -= amount

    def get_balance(self):
        return self.balance

def main():
    calculator = PersonalFinanceCalculator()
    calculator.add_income(2000)
    print("Доход:", calculator.income)
    print("Баланс:", calculator.get_balance())
    calculator.add_expense(1000)
    print("Расходы:", calculator.expenses)
    print("Баланс:", calculator.get_balance())
if __name__ == '__main__':
    main()
