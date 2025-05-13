from bank import Bank

def main():
    bank = Bank()
    while True:
        print("\n===== Bank Menu =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Account")
        print("6. View All Accounts")
        print("7. Exit")
        
        user_choice = int(input("Please enter your choice(1-7):"))

        if user_choice == 7:
            break

if __name__ == "__main__":
    main()