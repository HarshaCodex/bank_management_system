class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positve")
        if self.__balance < amount:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        return self.__balance
    
    def get_balance(self):
        return self.__balance