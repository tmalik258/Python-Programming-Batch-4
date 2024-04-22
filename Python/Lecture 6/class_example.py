class BankAccounts:
    # Class Represent a your Bank Account.
    def __init__(self, balance = 0):
        # Initilize the bank account class with starting balance is 0
        self.balance = balance
    
    def deposit(self, amount):
        # Deposit an amount into the bank account.
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("Invalid deposit amount")
            return False
        
    def withdraw(self, amount):
        #Withdraw an amount from the account
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Invalid withdraw ammount")
            return False
    def get_balance(self):
        # Return the current balance
        return self.balance

my_account = BankAccounts(1000)

my_account.deposit(500)
print(f"Current Balance: {my_account.get_balance()} " )

my_account.withdraw(250)
print(f"Current Balance Now: {my_account.get_balance()} ")