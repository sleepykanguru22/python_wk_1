# Create a BankAccount class with the attributes interest rate and balance
class BankAccount:
    total_accounts = []
    def __init__(self, int_rate, balance):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.total_accounts.append(self)

    def deposit(self, amount):
        # increases the account balance by the given amount
        self.balance += amount
    
    def withdraw(self, amount):
    #  decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        if (self.balance - amount) <= 0:
            self.balance -= 5
            print("Insufficient Funds: Charging $5")
        else:
            self.balance - amount

    def dislay_account_info(self):
        #  print to the console: eg. "Balance: $100"
        print(f"{self.balance}" ) 
    
    def yeild_interest(self):
    # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
    

acct_1 = BankAccount()
acct_2 = BankAccount()

acct_1.deposit(1000).deposit(300).deposit(500).withdraw(700).yeild_interest().display_account_info()

acct_2.deposit(5000).deposit(5000).withdraw(400).withdraw(200).withdraw(400).withdraw(200).yeild_interest().display_account_info()