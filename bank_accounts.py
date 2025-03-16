class Bank_account:
    def __init__(self, intamount, accname):
        self.balance = intamount
        self.name = accname
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        
    def get_balance(self):
        print(f"Account '{self.name}' Balance = ${self.balance:.2f}")