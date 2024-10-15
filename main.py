from account import Account

account = Account()

account.deposit(2000)
account.deposit(1000)
account.withdraw(500)

print(account.statement())
