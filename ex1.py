class BankAccount:
    def  __init__(self ,balance,client_name) -> None:
        self.balance=balance
        self.client_name=client_name
    def __deposit(self,amount):
        self.balance+=amount
    def getinformation(self)->None:
        return f"Client name:{self.client_name},balance:{self.balance}"
    def increase_balance(self,key,amount):
        if key=="@bankemp":
            self.__deposit(amount) 
account =BankAccount(200000,"Kitty")
account.client_name="Coca"
account.balance=4400000
account.increase_balance("@bankemp",30000)
print(account.getinformation())