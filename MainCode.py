print("Enter the name of account holder")
c = input("Enter the name: ")
d = int(input("Enter the balance: "))

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def obj(self):
        print(f"Account owner: {self.owner}")
        print(f"Account balance: {self.balance}")

    def deposit(self, x):
        self.balance += x
        print("Deposit Accepted")
        print("Current balance: {}".format(self.balance))

    def withdraw(self, y):
        if y > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= y
            print("Withdrawal Accepted")
        print("Current balance: {}".format(self.balance))


my_account = Account(c, d)

def system():
    print("WELCOME DEAR CUSTOMER!!!")
    print("Which service do you want from us ???")
    print("1. Cash withdrawal  2. Cash deposit  3. Balance enquiry")

    m = int(input("Enter the option 1, 2 or 3: "))
    if m == 1:
        a = int(input("Enter the withdrawl amount: "))
        my_account.withdraw(a)
    elif m == 2:
        a = int(input("Enter the deposit amount: "))
        my_account.deposit(a)
    elif m == 3:
        print("Current balance: {}".format(my_account.balance))
    else:
        print("Oops.. Enter valid input 1, 2 or 3")

def repeat():
    system()  
    print('Do you want to start the service again??')
    b = input("Enter YES or NO: ").upper()
    if b != 'YES':
       print("THANKS FOR VISITING US")
    else:
        repeat()   

repeat()
