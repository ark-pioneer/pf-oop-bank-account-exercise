class Account():
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def statement(self):
        return "Balance: " + str(self.balance)