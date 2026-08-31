class BankAccount:
    def  __init__(self,account_number,owner_name,balance):
        self.account_number = account_number,
        self.balance = balance 
        self.owner_name = owner_name

    def deposit(self, amount):
        self.balance += amount 
    
    def withdrwal(self,amount):
        if amount > self.balance:
            print("insuffecient balance")
        else :
            self.balance -= amount   
    
    def remain_balance(self):
        return self.balance 
    

bk=BankAccount(23445,"Dhruv",4558830)

bk.deposit(7000)
bk.withdrwal(1000)
print(bk.remain_balance())


        