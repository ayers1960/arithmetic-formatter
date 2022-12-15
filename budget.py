class Category:
  def __init__(self,category):
    self.category = category
    self.ledger = []
    
  def deposit(self,amount,description=""):
    self.ledger.append({"amount": amount, "description": description})
  
  def withdraw(self, amount, description = None):
    retVal = False
    if self.check_funds(amount):
      amount = -1 * amount;
      self.ledger.append({"amount": amount, "description": description})
      retVal = True
    return retVal
  
  def get_balance(self):
    balance = 0
    for r in self.ledger:
      balance += float(r['amount'])
    return balance
  
  def transfer(self, amount, category ):
    retVal = False
    if self.check_funds(amount):
      description = f"Transfer to {category}"
      self.ledger.append({"amount": -1*amount, "description": description})
      description = f"Transfer from {self.category}"
      self.deposit(amount, description)
      retVal = True
    return retVal
  
  def check_funds(self, amount):
    balance = self.get_balance()
    return (amount <= balance)



def create_spend_chart(categories):
  pass
