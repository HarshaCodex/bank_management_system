from bank import Bank
import os

def main():
    bank = Bank()
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        
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
            break
        elif user_choice == 1:
            account_type = input("Savings or Checking Account: ").lower()
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
        else:
            print("Please enter options from 1-7 only")


if __name__ == "__main__":
    main()