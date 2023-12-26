from typing import List

class BankAccount:
    """
    This Class for work about Account bank
    """
    account_numbers: List[int] = []
    last_num = 999
    def __init__(self, name: str) -> None:
        self.name = name
        self.balance: int = 0
        self.id_bank: int = id(self) # BankAccount.last_num
        BankAccount.last_num += 1
        BankAccount.account_numbers.append(id(self))
        
        
    
    def show_display(self) -> None:
        print(25 * "-")
        print(f"hi, {self.name}\nYour current balance: {self.balance}")    
        print(25 * "-")


    def dopsit(self) -> None:
        amount = float(input("please enter amount to deposit: "))
        self.balance += amount
        self.show_display()
    

    def withdraw(self):
        amount_wd = float(input("please enter amount to withdarw: "))
        if self.balance > amount_wd:
            self.balance -= amount_wd
            self.show_display()


def main():
    ali = BankAccount("ali")
    print(25 * "+")
    print(f"your id number is {ali.id_bank}")
    print(25 * "+")
    
    while True:
        user_choice = int(input("Enter your option\n1- see balance\n2- deposit\n3- withdraw\n4- exit\nPlease Choice: "))
        if user_choice == 1:
            ali.show_display()

        elif user_choice == 2:
            ali.dopsit()

        elif user_choice == 3:
            ali.withdraw()
            
        elif user_choice == 4:
            print(f"bye {ali.name}")
            break
    

# ----------------------------------
if __name__ == "__main__":
    main()
    # ---------
    a = BankAccount("a")
    b = BankAccount("b")
    print(BankAccount.account_numbers)