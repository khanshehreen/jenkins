import unittest

from bank import BankAccount

class AccountBalanaceTestCase(unittest.TestCase):
    def setUp(self):
        self.user_account = BankAccount()

    def test_balance(self):
        self.assertEqual(self.user_account.balance, 3000, msg='Account Balance Invalid.')

    def test_deposit(self):
        self.user_account.deposit(4000)
        self.assertEqual(self.user_account.balance, 7000, msg='Deposit Method Inaccurate.')

    def test_withdraw(self):
        self.user_account.withdraw(500)
        self.assertEqual(self.user_account.balance, 2500, msg='Withdraw method Inaccurate.')

    def test_invalid_transaction(self):
        self.assertEqual(self.user_account.withdraw(6000), "Invalid Transaction", msg='Invalid Transaction.')

if __name__ == '__main__':
    unittest.main()
