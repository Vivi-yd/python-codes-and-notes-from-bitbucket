class BankAccount:
    
    total_penalty_for_all = 0 ## This is a class attributes   
    
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        
        self.balance = initial_balance
        
        self.penalty = 5  ### These are object attributes
        self.total_penalty = 0
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance += amount
        
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        
        
        if amount > self.balance: 
            self.balance -= (amount + self.penalty)
            self.total_penalty += self.penalty
            BankAccount.total_penalty_for_all += self.penalty
        else:
            self.balance -= amount
            
        
            
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
    
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.total_penalty ## Here the attributes of each 
                                  ## different object is being return
    
### Then how do I return the class attributes, I meant how
### to get the program prints the total penalties of all account
### combined.
    

account1 = BankAccount(20)
account1.deposit(10)
account2 = BankAccount(10)
account2.deposit(10)
account2.withdraw(50)
account1.withdraw(15)
account1.withdraw(10)
account2.deposit(30)
account2.withdraw(15)
account1.deposit(5)
account1.withdraw(10)
account2.withdraw(10)
account2.deposit(25)
account2.withdraw(15)
account1.deposit(10)
account1.withdraw(50)
account2.deposit(25)
account2.deposit(25)
account1.deposit(30)
account2.deposit(10)
account1.withdraw(15)
account2.withdraw(10)
account1.withdraw(10)
account2.deposit(15)
account2.deposit(10)
account2.withdraw(15)
account1.deposit(15)
account1.withdraw(20)
account2.withdraw(10)
account2.deposit(5)
account2.withdraw(10)
account1.deposit(10)
account1.deposit(20)
account2.withdraw(10)
account2.deposit(5)
account1.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account2.deposit(10)
account2.deposit(15)
account2.deposit(20)
account1.withdraw(15)
account2.deposit(10)
account1.deposit(25)
account1.deposit(15)
account1.deposit(10)
account1.withdraw(10)
account1.deposit(10)
account2.deposit(20)
account2.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account1.deposit(10)
account2.withdraw(20)
print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()

#expected result -55 45 45 20 :)