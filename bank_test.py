import unittest
# import pytest
from bank import Bank_Account

class Test_Bank_Account(unittest.TestCase):

    def test_deposit(self):
        account = Bank_Account(opening_balance=100) 
        account.deposit(100)
        assert account.get_balance() == 200
        

    def test_deposit_zero(self):
        account = Bank_Account(opening_balance=100)
        with self.assertRaises(ValueError):
            account.deposit(0)

    def test_deposit_negative(self):
        account = Bank_Account(opening_balance=100)
        with self.assertRaises(ValueError):
            account.deposit(-10)
    
    def withdraw(self):
        account = Bank_Account(opening_balance=100)
        account.withdraw(50)
        assert account.get_balance() == 50


    def test_withdraw_zero(self):
        account = Bank_Account(opening_balance=100)
        with self.assertRaises(ValueError):
            account.withdraw(0)

    def test_withdraw_negative(self):
        account = Bank_Account(opening_balance=100)
        with self.assertRaises(ValueError):
            account.withdraw(-10)

    def test_withdraw_closed_Account(self):
        account = Bank_Account(opening_balance=100)
        account.close_account()
        with self.assertRaises(RuntimeError):
            account.withdraw(10)

    def test_withdraw_insuffient_funds(self):
        account = Bank_Account(opening_balance=100)
        with self.assertRaises(ValueError):
            account.withdraw(150)

    def test_get_balance_closed_account(self):
        account = Bank_Account(opening_balance=100)
        account.close_account()
        with self.assertRaises(RuntimeError):
            account.get_balance()
            
    def test_withdraw(self):
        account = Bank_Account(opening_balance=100)
        account.withdraw(100)
        assert account.get_balance() == 0

if __name__ == '__main__':
    unittest.main()


    

