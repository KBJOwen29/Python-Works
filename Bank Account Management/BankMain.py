import BankAccounts as BA
import BankClasses as BC

#Main System Loop
def main_system():
    print("Welcome to the Bank Account Management System")
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            acc_num = input("Enter Account Number: ")
            acc_holder = input("Enter Account Holder Name: ")
            account = BA.Account(acc_num, acc_holder)
            initial_balance = float(input("Enter Initial Balance: "))
            print(account.set_initial_balance(initial_balance))
        
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            transaction = BC.Transaction()
            print(transaction.deposit(amount))
        
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            transaction = BC.Transaction()
            print(transaction.withdraw(amount))
        
        elif choice == '4':
            print(f"Current Balance: {account.get_balance()}")
        
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
main_system()