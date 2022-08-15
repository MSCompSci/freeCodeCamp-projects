class Category:


  def __init__(self,Category): #define class variables
    self.Category = Category #Categories of things
    self.ledger = [] #The ledger of all transactions
    self.total = 0 #Total for checking funds
    self.lines = "" #Lines of print out

  def __str__(self): #prints out table when class object printed
    self.stars = (30 - len(str(self.Category)))//2
    self.header = self.stars*"*"+str(self.Category)+self.stars*"*"+"\n"
    self.footer = "Total: "+"{:4.2f}".format(Category.get_balance(self))
    for i in self.ledger:
      self.amnt = "{:4.2f}".format(float(i["amount"]))
      self.desc = str(i["description"][0:23])
      self.spaces = 30- (len(self.amnt)+len(self.desc))
      self.lines += self.desc + self.spaces*" " +self.amnt +"\n"
    return self.header+self.lines+self.footer
  

  def transfer(self,amount,othercat): #Transfer of funds from one category to another
    if Category.check_funds(self,amount):
      Category.withdraw(self,amount,"Transfer to "+othercat.Category)
      othercat.deposit(amount,"Transfer from "+self.Category)
      return True
    return False




  def deposit(self,amount,description=""): #Deposit of funds into a category
    self.ledger.append( {"amount":amount,"description":description})

  def withdraw(self,amount,description=""): #Withdrawl of funds from a category
    if Category.check_funds(self,amount):
      self.ledger.append( {"amount":0-amount,"description":description})
      return True
    return False
    
  
  def get_balance(self): #Prints balance
    self.balance = 0
    for i in self.ledger:
      self.balance += i["amount"]
    return self.balance




    
  def check_funds(self,amount): #Checks funds available for use
    for i in self.ledger:
      self.total += i["amount"]
    if (self.total - amount)>0:
      return True
    return False
  


def create_spend_chart(categories): #Creates a chart of spendature percentages
  import math
  head = "Percentage spent by category"
  led={}
  words = []
  totalbycat = 0
  total = 0
  wordline = ""
  chart = ""
  longest = 0
  count = 0

  for i in categories:
    for x in i.ledger:
      val = x["amount"]
      if val<0:
        total += val
        totalbycat +=val
    led[i.Category]=totalbycat
    totalbycat = 0
    if len(i.Category)>longest:
      longest = len(i.Category)

  for y in led:
    led[y] = (led[y]/total)*10
    led[y] = math.floor(led[y])


  for x in range(100,-10,-10):
    spaces =10
    line = "{:>4}".format(str(x)+"|")
    for z in led:
      if (led[z] == (x/10)):
        line += " o "
        spaces-=3
        led[z]-=1
      else:
        line+="   "
        spaces-=3

    chart+=line+spaces*" "+"\n"
  chart+="    ----------"


  for x in range(longest): 
    words.append([])
    for i in range(len(categories)):
      words[x].append(" ")





  for i in categories:
    for y in range(len(i.Category)):
      words[y][count] = i.Category[y]
    count+=1

  for w in words:
    wordline+="     "
    for l in w:
    
      wordline+=l+"  "
    wordline+="\n"
  wordline = wordline[:-1]


  return head+"\n"+chart+"\n"+wordline

