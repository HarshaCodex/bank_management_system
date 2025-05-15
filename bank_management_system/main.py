from bank import Bank
import os

def main():
    bank = Bank()
    bank.load_from_file("accounts.pkl")
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n===== Bank Menu =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Account")
        print("6. View All Accounts")
        print("7. Exit")
        
        try:
            user_choice = int(input("Please enter your choice(1-7):"))
        except ValueError:
            print("Enter only number from 1-7 only")
            continue

        if user_choice == 7:
            bank.save_to_file("accounts.pkl")
            break
        elif user_choice == 1:
            account_type = input("Savings or Checking Account: ").strip().lower()
            account_number = int(input("Please enter desired account number: "))
            account_holder = input("Please enter the name of account holder: ")
            balance = float(input("Enter the amount to deposit: "))
            if account_type == "checking":
                extra_info = float(input("Enter overdraft limit for your checking account: "))
            elif account_type == "savings":
                extra_info = float(input("Enter interest rate for your savings account: "))
            else:
                raise ValueError("Please create either savings or checking account only")
            
            try:
                bank.create_account(account_type, account_number, account_holder, balance, extra_info)
                print("Account created successfully")
            except ValueError as e:
                print(f"Error: {e}")
        elif user_choice == 2:
            account_number = int(input("Please enter the account number to deposit: "))
            deposit_amount = float(input("Please enter amount to deposit: "))
            try:
                account = bank.get_account(account_number)
                account.deposit(deposit_amount)
                print("Amount deposited successfully")
                print(f"Your balance:{account.balance}")
            except ValueError as e:
                print(f"Error: {e}")
        elif user_choice == 3:
            account_number = int(input("Please enter the account number to withdraw: "))
            withdraw_amount = float(input("Please enter amount to withdraw: "))
            try:
                account = bank.get_account(account_number)
                account.withdraw(withdraw_amount)
                print("Amount wihdrawn successfully!")
                print(f"Your balance:{account.balance}")
            except ValueError as e:
                print(f"Error: {e}")
        elif user_choice == 4:
            from_account = int(input("Enter your account number to transfer from: "))
            to_account = int(input("Enter the account number to transfer to: "))
            transfer_amount = float(input("Enter amount to transfer: "))
            try:
                bank.transfer(from_account, to_account, transfer_amount)
                from_account = bank.get_account(from_account)
                print("Amount transferred successfully!")
                print(f"Your updated balance:{from_account.balance}")
            except ValueError as e:
                print(f"Error: {e}")
        elif user_choice == 5:
            account_number = int(input("Enter the account number to view: "))
            try:
                account = bank.get_account(account_number)
                print("\n===== Account Details =====")
                print(f"Account Number : {account.account_number}")
                print(f"Account Holder : {account.account_holder}")
                print(f"Account Type   : {type(account).__name__}")
                print(f"Balance        : {account.balance}")

                if hasattr(account, 'interest_rate'):
                    print(f"Interest Rate  : {account.interest_rate}")
                if hasattr(account, 'overdraft_limit'):
                    print(f"Overdraft Limit: {account.overdraft_limit}")
            except ValueError as e:
                print(f"Error: {e}")
        elif user_choice == 6:
            bank.show_all_accounts()
        else:
            print("Please enter options from 1-7 only")

        input("Please enter to continue")


if __name__ == "__main__":
    main()