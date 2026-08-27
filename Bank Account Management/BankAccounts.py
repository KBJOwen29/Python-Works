# For Accounts
class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # Gets the balance of the signed in account
    def get_balance(self):
        return self.balance

    # Sets the name of the Account
    def set_Name(self, new_name):
        self.account_holder = new_name

    # Sets the Account Number
    def set_accountNumber(self, new_account_number):
        self.account_number = new_account_number

    # Gets the information of the Account
    def get_AccountInfo(self):
        return {
            "Account Number": self.account_number,
            "Account Holder": self.account_holder,
            "Balance": self.balance
        }
        
    # Sets an initial balance to a newly created account    
    def set_initial_balance(self, amount):
        if amount >= 0:
            self.balance = amount
            return f"Initial balance set to {self.balance}"
        else:
            return "Initial balance cannot be negative"
        
