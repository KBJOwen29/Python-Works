import BankAccounts as BA


class Transaction:

    # Withdraws a certain amount of money from your balance
    def withdraw(self, amount):
        if amount > BA.self.balance:
            return "Insufficient funds"
        elif amount <= 0:
            return "Invalid withdrawal amount"
        elif amount < BA.self.balance:
            BA.self.balance -= amount
            return f"Withdrew {amount}. New balance is {BA.self.balance}"
        else:
            return "Error in withdrawal"

    # Deposits a certain amount of money to your balance
    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount"
        elif amount > 0:
            BA.self.balance += amount
            return f"Deposited {amount}. New balance is {BA.self.balance}"
        else:
            return "Error in deposit"
        
