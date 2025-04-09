class BalanceException(Exception):
    pass

class Bank_account:
    def __init__(self, intamount, accname):
        self.balance = intamount
        self.name = accname
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        
    def get_balance(self):
        print(f"Account '{self.name}' Balance = ${self.balance:.2f}")
    
    def deposit(self,amount):
        self.balace =self.balance + amount
        print("depositis compleate.")
        self.get_balance()
        
    def viableTranceAction(self,amount):
       if self.balance >= amount:
           return
       else:
           raise BaseException(
               f"\nSorry, account '{self.name}' only have a balace of{self.balance:.BlanceException}"
           )
           
    def withdraw(self, amount):
        try:
            self.viableTranceAction(amount)
            self.balance = self.balance - amount 
            print("\n withdraw complite")
            self.get_balance()
        except BalanceException as error:
            print(f"\nwithdraw interrupted: {error}")