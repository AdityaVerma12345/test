class bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.history = []
        self.idk=[]
    def add(self,amt):
        if amt <= 0:
            print( "Error")
        else:
            self.balance=self.balance+amt
            self.history.append(self.balance)
            print("depost +",amt)
    def sub(self,amt):
        if amt>self.balance :
            print("Insufficient funds")
        else:
            self.balance=self.balance-amt
            self.history.append(self.balance)
            print("Withdraw -",amt)
acc = bank("Sam", 100)
acc.add(50)
acc.sub(30)
acc.sub(500)   # should say insufficient funds
acc.add(-10)    # should say invalid
print(acc.history)
print(acc)
        