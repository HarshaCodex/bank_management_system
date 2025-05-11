class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount
        transaction_log = {"type": "Deposit", "amount": amount, "balance": self.balance}
        self.transaction_history.append(transaction_log)
        return self.__balance
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        if self.__balance < amount:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        transaction_log = {"type": "Withdraw", "amount": amount, "balance": self.balance}
        self.transaction_history.append(transaction_log)
        return self.__balance
    
    @property
    def balance(self):
        return self.__balance
    
    def get_transaction_history(self):
        return self.transaction_history