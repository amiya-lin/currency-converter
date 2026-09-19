class bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

ac1 = bankaccount("xm",1000)



ac1.deposit(1000)

print(ac1.balance)