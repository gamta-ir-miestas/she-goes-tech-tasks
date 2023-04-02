# Create a class named BankAccount that has the 
# following attributes: account_number, balance, and 
# owner_name. It should also have methods called 
# deposit() and withdraw() that update the balance 
# accordingly.

class BankAccount:

    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self, money):
        self.balance += money
        return self.balance

    def withdraw(self, money):
        self.balance -= money
        return self.balance

    def account_info(self):
        return self.account_number, self.balance, self.owner_name

account1 = BankAccount("5972684785691234", 100, "Name Surname")
account1.deposit(100)
account1.withdraw(15)
print(account1.account_info())