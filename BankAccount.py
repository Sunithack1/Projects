''' Creating a bank account program that does the fllowing:
- Accepting deposits
- Allowing withdrawals
- Showing the balance
- Showing the details of the account'''

class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "Name: %s, Balance = $%0.2f" % (self.name, self.balance)
  def show_balance(self): #shows the balance
    print "Balance = $%0.2f" % self.balance
  def deposit(self, amount): #deposits the amount
    #self.amount = amount
    if amount <= 0:
      print "Invalid amount!"
      return
    else: 
      print "Deposited amount = $%0.2f" % amount
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount): #amount withdraw
    #self.amount = amount
    if amount > self.balance:
      print "Insufficient balance"
      return
    else:
      print "Withdrawal Amount = $%0.2f" % amount
      self.balance -= amount
      self.show_balance()
my_account = BankAccount("Sunitha")
print my_account  
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account