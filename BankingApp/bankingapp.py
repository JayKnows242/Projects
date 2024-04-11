import os

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Customer(Person):
    def __init__(self, first_name, last_name, account_number, balance=0.0):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Customer: {self.first_name} {self.last_name}\nAccount Number: {self.account_number}\nBalance: ${self.balance:.2f}"

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

def clear_screen():
    # Clear the screen depending on the OS
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()  # Clear the screen at the beginning
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    account_number = input("Enter account number: ")
    customer = Customer(first_name, last_name, account_number)

    while True:
        clear_screen()  # Clear the screen before showing menu
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Print Information")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            customer.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            customer.withdraw(amount)
        elif choice == '3':
            print(customer)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        input("Press Enter to continue...")  # Wait for user to press Enter before clearing screen

    clear_screen()  # Clear the screen before exiting

if __name__ == "__main__":
    main()
