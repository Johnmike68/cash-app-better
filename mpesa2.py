class mpesa():
    def __init__(self,phone,balance):
        self.phone = phone
        self.balance = balance

    def get_balance(self):
        print(f" your mpesa balance is {self.balance}")

    def withdraw(self,withdr):
        print(f"{withdr} will be removed from ur balance!!!")
        print(f"your new balance is: {self.balance-withdr}")

    def deposit(self,amount):
        print(f"{amount} will be added into ur balance")
        print(f"your new balance is {amount+self.balance}")

def menu():
    print("""
    -------------------------Welcome to mpesa---------------------------------
        1.press 1 to deposit money.
        2.press 2 to withdraw money.
        3.press 3 to check balance.
        4.press 4 to exit
        
    -------------------------welcome again------------------------------------""")

def act():
    account=mpesa("0792355950",balance=6000)
    menu()
    while True:
        user_choice = int(input("what whould u like from our menu ?\n"))
        if user_choice==1:
            depo = int(input('what amount would u like to deposit:\n'))
            return account.deposit(depo)
            menu()
        elif user_choice==2:
            withdr = int(input("how much would u like to withdraw?\n"))
            return account.withdraw(withdr)
            menu()
        elif user_choice==3:
            return account.get_balance(balance)
            menu()
        elif user_choice==4:
            break
        else:
            return f"entered value incorrect"
            menu()


act()



    

