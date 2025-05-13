from accounts import Account

class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Enter positive amount only")
        if self.balance + self.overdraft_limit < amount:
            raise ValueError("Insufficent funds including overdraft limit")
        self.balance -= amount
        transaction_log = {"type": "Withdraw", "amount": amount, "balance": self.balance}
        self.transaction_history.append(transaction_log)
        return self.balance