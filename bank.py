import random

class BankAccount: 
    def __init__(self, full_name):
        self.full_name = full_name
        # only fullname goes in the parameters because the user inputs that 
        self.account_number = random.randint(0, 999999)
        self.routing_number = 987654321
        self.balance = 0
        

# deposit method
    def deposit(self, amount):
        
        self.balance += amount
        print(f"Amount Deposited: ${amount}")


    def withdraw(self,amount):
        self.balance -= amount

my_account = BankAccount("Rafa Vazquez")

print(my_account.full_name)
print(my_account.routing_number)
print(my_account.account_number)
print(my_account.balance)