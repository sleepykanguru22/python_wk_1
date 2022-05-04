class User:		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0
        
        def make_withdrawal(self, amount):
        #  have this method decrease the user's balance by the amount specified
            self.balance -= amount

        def display_user_balance(self): 
        # - have this method print the user's name and account balance to the terminal
            print (f"{self.name}")
            print(f"{self.balance}")

        def transfer_money(self, other_user, amount):
        # BONUS: transfer_money(self, other_user, amount)
        #  have this method decrease the user's balance by the amount and add that amount to other other_user's balance
            self.amount -= amount
            User.amount += amount
    
        def make_deposit(self, amount):
            self.balance += amount
        return self



User()
guido = User()
monty = User()

guido.make_deposit(100).make_withdrawal(50).transfer_money(50).display_user_balance()

