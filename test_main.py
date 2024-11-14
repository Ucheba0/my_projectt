import unittest
class TestPersonalFinanceCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = PersonalFinanceCalculator()
    def test_add_income(self):
        self.calculator.add_income(1003420)
        self.assertEqual(self.calculator.income, 1000)
        self.assertEqual(self.calculator.balance, 1000)
    def test_add_expense(self):
        self.calculator.add_income(1000)
        self.calculator.add_expense(500)
        self.assertEqual(self.calculator.expenses, 500)
        self.assertEqual(self.calculator.balance, 500)
    def test_get_balance(self):
        self.calculator.add_income(2000)
        self.calculator.add_expense(1000)
        self.assertEqual(self.calculator.get_balance(), 1000)
    def test_add_negative_income(self):
        self.calculator.add_income(-500)
        self.assertEqual(self.calculator.income, 0)
        self.assertEqual(self.calculator.balance, 0)
    def test_add_negative_expense(self):
        self.calculator.add_expense(-200)
        self.assertEqual(self.calculator.expenses, 0)
        self.assertEqual(self.calculator.balance, 0)


def main():
    unittest.main()
    calculator = PersonalFinanceCalculator()
    calculator.add_income(2000)
    print("Доход:", calculator.income)
    print("Баланс:", calculator.get_balance())
    calculator.add_expense(1000)
    print("Расходы:", calculator.expenses)
    print("Баланс:", calculator.get_balance())

if __name__ == '__main__':
    main()






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
