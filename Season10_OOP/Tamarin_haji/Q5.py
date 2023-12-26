import os
os.system("cls")

class BankAccount:
    def __init__(self, balance, name) -> None:
        self.name = name
        self.balance = balance

    def __str__(self) -> str:
        return f"Owner: {self.name} | Balance: {self.balance}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.balance}, {self.name})"
    
    def __eq__(self, other) -> bool:
        self.balance == other.balance

    def __add__(self, other):
        return BankAccount(self.balance + other.balance,\
                           self.name + "-" + other.name)
    
    def __iadd__(self, other):
        self.balance += other.balance
        other.balance = 0
        return self
    
    def deposit(self, value):
        self.balance += value
        return self
    
    def withdraw(self, value):
        if value < self.balance:
            self.balance -= value
        return self
    
    def transfer(self, other, price):
        if price < self.balance:
            self.balance -= price
            other.balance += price
        return self

a = BankAccount(100, "ali")
b = BankAccount(120, "akbar")
a+=b
print(b)