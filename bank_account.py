class BankAccount:
    def __init__(self, balance=0.0):
        """Initialize the bank account with an optional starting balance."""
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Invalid withdrawal amount or insuffucient funds.")

    def display_balance(self):
        """Show the current balance."""
        print(f"Current Balance: ${self.balance:.2f}")
