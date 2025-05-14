from accounts import SavingsAccount, CheckingAccount

class Bank:

    def __init__(self):
        self.__accounts = {}

    def create_account(self, account_type, account_number, account_holder, balance, extra_info):
        if account_number in self.__accounts:
            raise ValueError("Account with this number already exists!")
        if account_type == 'savings':
            account = SavingsAccount(account_number, account_holder, balance, extra_info)
        elif account_type == "checking":
            account = CheckingAccount(account_number, account_holder, balance, extra_info)
        else:
            raise ValueError("Create either checking or savings account")
        
        self.__accounts[account_number] = account
        return account
    
    def get_account(self, account_number):
        if account_number in self.__accounts:
            return self.__accounts[account_number]
        else:
            raise ValueError("Account not found")
    
    def transfer(self, from_acc_number, to_acc_number, amount):
        from_acc = self.get_account(from_acc_number)
        to_acc = self.get_account(to_acc_number)
        from_acc.withdraw(amount)
        to_acc.deposit(amount)
    
    def show_all_accounts(self):
        if not self.__accounts:
            print("No Accounts avaialble")
            return None
        for account in self.__accounts.values():
            print(f"Account Number:{account.account_number}")
            print(f"Account Holder:{account.account_holder}")
            print(f"Balance:{account.balance}")


        
    

