class bank_account:
    def __init__(self,bal):
        self.bal=bal
    def deposit(self,amt):
        self.bal+=amt
        print("amount deposited")
    def withdrawal(self,amt):
        if amt>(self.bal):
            print("insufficient balance")
        else:
            self.bal=self.bal-amt
            print("amount withdrawn")
b=bank_account(0)

while True:
    n=int(input("enter your choice 1. deposit 2.withdrawal 3.exit "))
    if n==1:
        amt=int(input("enter your amount for deposit"))
        b.deposit(amt)
    elif n==2:
        amt=int(input("enter amount for withdrawal"))
        b.withdrawal(amt)
    elif n==3:
        break
    else:
        continue
        