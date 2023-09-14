class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ₹{self.__account_balance}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create a BankAccount instance
    my_account = BankAccount("123456", "John Doe", 1000)

    # Display the initial balance
    my_account.display_balance()

    # Make a deposit
    my_account.deposit(500)

    # Make a withdrawal
    my_account.withdraw(200)

    # Try to withdraw an invalid amount
    my_account.withdraw(2000)

    # Display the updated balance
    my_account.display_balance()
