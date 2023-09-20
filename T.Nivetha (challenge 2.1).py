class BankAccount:
  
 def __init__(self, account_number, account_holder_name, initial_balance=0.0): 
   self.__account_number = account_number
   self.__acount_holder_name = account_holder_name
   self.__account_balance = initial_balance
  
 def deposit(self,amount):
   if amount > 0:
     self.__account_balance += amount
#self.__account_balance=self.__account_balance+amount
     print("Deposited ₹{}. New  balance{}".format(amount, self.__account_balance)) 
   else: 
     print("Invalid deposit amount.") 
    
 def withdraw(self, amount):
   if amount > 0 and amount <= self.__account_balance:
     self.__account_balance -= amount 
#self.__account_balance = self.__account_balance-amount
     print("withdraw ₹{}. New balanace:{}".format(amount, self.__account_balance))
   else:    
    print("Invaild withdrawl amount or insufficient balance.")
    
 def display_balance(self):
    print("Account Balance for {} (Account #{}): ₹{}".format(
      self._account_holder_name, self._account_number,
      self._account_balance))
  
# create an instance of the Bank Account class
account = BankAccount(account_number = "123456789",
                      account_holder_name = "nivetha",
                      intial_balance = 5000.0) 

#Test deposit and withdrawl functionality
account.display_balance()
account.deposit(5000)
account.withdraw(200.0) 
account.display_balance()