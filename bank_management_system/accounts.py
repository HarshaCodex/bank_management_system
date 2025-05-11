class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance
    
    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            print(f"Balance after deposit:{self.__balance}")
        else:
            print("Enter positive amount")
    
    def withdraw(self, amount):
        if amount >= 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Balance after withdraw:{self.__balance}")
            else:
                print("Not enough balance")
        else:
            print("Enter positive amount")
    
    def get_balance(self):
        print(f"Your balance:{self.__balance}")