class Bank_Account():
    def __init__(self , opening_balance ):
        self.balance = opening_balance
        self.closed = False
    
    def deposit(self, amount):
        if amount <=0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <=0:
            raise ValueError("Withdrawal must be positive")
        if self.closed:
            raise RuntimeError("Account is closed")
        if amount > self.balance:
            raise ValueError("Insuffient funds")
        self.balance -= amount

    def close_account(self):
        self.closed = True
    
    def get_balance(self):
        if self.closed:
            raise RuntimeError("Account is closed")
        return self.balance




        