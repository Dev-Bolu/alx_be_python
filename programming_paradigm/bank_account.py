class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance #Encapsulation using double underscore
        
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance +=amount
        else:
            print('Deposit must be positive')
    
    def withdraw(self, amount):
        if amount > self.__account_balance:
            return False #Insufficient Funds
        elif amount <=0:
            print("Withdrawal amount must be positive")
        else:
            self.__account_balance -= amount
            return True
        
    def display_balance(self):
        self.__account_balance = self.__account_balance if self.__account_balance >= 0 else 0
        # Display the balance with two decimal places
        print(f"Current Balance: #{self.__account_balance:.2f}")
        
        
    
        