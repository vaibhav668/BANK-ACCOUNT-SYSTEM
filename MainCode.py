print("Enter the name of account holder")
c=input("enter the name")
d=int(input("enter the balance"))
class   Account:
        def __init__(self,owner,balance):
            self.owner=owner
            self.balance=balance
        def obj(self):
            print(f"Account owner: {self.owner}")
            print(f"Account balance: {self.balance}")
        def deposit(self,x):
            self.x=x
            self.balance+=x
            print("Deposit Accepted")
            print("current balance: {}".format(self.balance))
        def withdraw(self,y):
            self.y=y
            if y>self.balance:
               print("Funds Unavailable!")
               print("current balance: {}".format(self.balance))
            else:
                self.balance=self.balance-y
                print("Withdrawl Accepted")
                print("current balance: {}".format(self.balance))
my_account=Account(c,d)             
def system():
    print("WELCOME DEAR CUSTOMER!!!")
    print("Which service do yo want from us ???")
    print("1.cash withdrawl  2.cash deposit  3.balance enquiry")
    m=int(input("Enter the option 1,2 or 3"))
    if m==1:
       a=int(input("enter the withdrawl amount"))
       my_account.withdraw(a)
    elif m==2:
         a=int(input("enter the deposit amount"))
         my_account.deposit(a)   
    elif m==3:
         print("current balance: {}".format(my_account.balance))
    else:
        print("oops..enter valid input 1,2 or 3")     

def repeat():
    while True:
          print('Do you want to start the service again??')
          b=input("enter yes or no").upper()
          if b=='YES':
             system()
          else:
               print("THANKS FOR VISITING US")   
               break
        
system()
repeat()