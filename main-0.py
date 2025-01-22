import sys
from bank_account import BankAccount  

def main():
    # Initialize a BankAccount object
    account = BankAccount() 

    #Ensure at least one argument is provided (operation type)
    if len(sys.argv) < 2:
        print("Usage: python main.py<operation>:[amount]")
        print("Operations: deposit, withdraw, display")
        return
    
    # Extract operation and optional amount
    operation = sys.argv[1].lower()
    amount = float(sys.argv[2]) if len(sys.argv) > 2 else None
        
    if operation == "deposit":
        if amount is not None:
            print(account.deposit(amount))
        else:
            print("Please provide an amount to deposit. ")    
        
    elif operation == "withdraw":
        if amount is not None :
            print(account.withdraw(amount))
        else:
            print("Please provide an amount to withdraw.")

    elif operation == "display":
        print(account.display())
    else:
        print("Invalid operation. Use: deposit, withdraw, or display.")
        
if __name__ == "__main__":
    main()