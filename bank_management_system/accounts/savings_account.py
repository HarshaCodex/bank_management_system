from accounts import Account 

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * (self.interest_rate/100)
        self.deposit(interest)
        print(f"Interst of {interest} applied to the account.")