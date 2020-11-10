import random

class BankAccount: 
    def __init__(self, full_name):
        self.full_name = full_name
        # only fullname goes in the parameters because the user inputs that 
        self.account_number = random.randint(10, 999999)
        self.routing_number = 987654321
        self.balance = 0

        

# deposit method
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}")


    def withdraw(self,amount):
        if amount > self.balance:
            self.balance -= amount
            print("Insuffient Funds")
            self.balance -= 10
            print(f'Amount Withdrawn: ${amount}')

        else:
            self.balance -= amount
            print(f'Amount Withdrawn: ${amount}')

    def get_balance(self):
        print(f"Thank you for using our service, your ending balance is ${self.balance}")
        # return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_reciept(self):
        print(self.full_name)
        print(f"Account No.: ${self.account_number}")
        print(f"Routing No.: ${self.routing_number}")
        print(f"Balance: ${self.balance}")


my_account = BankAccount("Rafa Vazquez")
friends_account = BankAccount("Tony lopes")
my2_account = BankAccount("Rafael Vazquez Navarro")

# print(my_account.get_balance)

# print(my_account.full_name)
print(my_account.account_number)
print(my2_account.account_number)


my_account.deposit(10)
my_account.get_balance()
my_account.print_reciept()
# print(my_account.get_balance)
# print(get_balance)

# my_account.withdraw(10)
# my_account.withdraw(10)

# friends_account.add_interest()
# friends_account.deposit(20)
# friends_account.account_number
# print(friends_account.account_number)


# print(my_account.balance)

