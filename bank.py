import random

class BankAccount: 
    def __init__(self, full_name):
        self.full_name = full_name
        # only fullname goes in the parameters because the user inputs that 
        self.account_number = random.randint(100000000, 999999999)
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
            print(f'Your account has been charged an overdraft fee of: $10')

        else:
            self.balance -= amount
            print(f'Amount Withdrawn: ${amount}')

            # call the bottom three methods in order for them to show in the terminal

    def get_balance(self):
        print(f"Thank you for using our service, your ending balance is ${self.balance}")
        # round({self.balance}, 2)
        # return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance = self.balance - interest

    def print_reciept(self):
        print(self.full_name)
        print(f"Account No.: {self.account_number}")
        print(f"Routing No.: {self.routing_number}")
        print(f"Balance: ${self.balance}")


my_account = BankAccount("Rafa Vazquez")
tony_account = BankAccount("Tony Grass")
sam_account = BankAccount("Sam Mas")

# print(my_account.full_name)
# print(tony_account.full_name)
# print(my_account.account_number)
# print(tony_account.routing_number)
# print(sam_account.balance)


# tony_account.deposit(10)
# my_account.deposit(10)
# my_account.get_balance()
# my_account.print_reciept()
# print(my_account.get_balance)
# print(get_balance)

# my_account.withdraw(10)
# my_account.withdraw(10)
# my_account.get_balance()

# tony_account.add_interest()
# tony_account.get_balance()
# tony_account.deposit(20)
# tony_account.account_number
# print(tony_account.account_number)


# print(my_account.balance)

