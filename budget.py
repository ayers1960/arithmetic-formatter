class Category:
  def __init__(self,category):
    self.category = category
    self.ledger = []

  def __str__(self):
    titleSize = 30
    descSize  = 23
    catLen = len(self.category)
    left = (titleSize - catLen)//2
    
    right = (titleSize - catLen)//2
    rightStr = "*"*right
    leftStr  = "*"*left
    retStr = f"{leftStr}{self.category}{rightStr}\n" 
    for r in self.ledger:
      retStr += f"{r['description'][0:descSize]:{descSize}s}"
      retStr += f"{float(r['amount']):7.2f}"
      retStr += "\n"
    balance = self.get_balance()
    retStr += f"Total: {balance:.2f}"
    return retStr
    
  def deposit(self,amount,description=""):
    self.ledger.append({"amount": amount, "description": description})
  
  def withdraw(self, amount, description = None):
    retVal = False
    if self.check_funds(amount):
      amount = -1 * amount;
      if description is None:
        description = ""
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
      description = f"Transfer to {category.category}"
      self.ledger.append({"amount": -1*amount, "description": description})
      description = f"Transfer from {self.category}"
      category.deposit(amount, description)
      retVal = True
    return retVal
  
  def check_funds(self, amount):
    balance = self.get_balance()
    return (amount <= balance)

  def amountSpent(self):
    spent = 0.0;
    for r in self.ledger:
      if r['amount'] < 0:
        spent += -1 * r['amount']     
    return round(spent,2)


def create_spend_chart(categories):
  totalSpent = 0.0;
  for C in categories:
    spent = C.amountSpent()
    totalSpent = round(totalSpent + spent,2)

  for C in categories:
    spent = C.amountSpent()
    C.percentSpent = 100.0*spent/totalSpent 

  retStr = "Percentage spent by category\n";
  for i in range(100,-10,-10):
    retStr += f"{i:3d}|"
    for C in categories:
      if C.percentSpent >= i:
        retStr += " o "
      else:
        retStr += "   "        
    retStr += " \n"
  retStr += "    "
  maxName = 0
  for C in categories:
    retStr += "-"*3
    maxName = max(maxName, len(C.category))
  retStr += "-\n"
  for i in range(0,maxName):
    retStr += "   "
    for C in categories:
      if i < len(C.category):
        retStr += f"  {C.category[i:i+1]}"
      else:
        retStr += f"   "
    retStr += "\n"

  print(retStr)
  return retStr
