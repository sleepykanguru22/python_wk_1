

# declare a class and give it name User
class User:		
    def __init__(self):
        self.name = name
        self.email = email
        self.account_balance = BankAccount(int_rate=0.02, balance=0)


    def make_deposit(self, amount):
    	self.account_balance += amount	

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self): 
        print (f"{self.name}")
        print(f"{self.account_balance}")

      
           
       
User()
guido = User()
monty = User()
# Accessing the instance's attributes
print(guido.name)	# output: Michael
print(monty.name)	# output: Michael

