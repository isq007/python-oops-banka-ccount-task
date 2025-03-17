class BankAccount:
    total_accounts = 0  # Class variable to track total accounts
    all_accounts = {}  # Dictionary to store all accounts
    
    def __init__(self, name, account_type, balance=0):
        if not name:
            raise ValueError("Account holder's name cannot be empty.")
        
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.transactions = []  # Store transaction history
        self.account_number = BankAccount.total_accounts + 1
        
        BankAccount.total_accounts += 1
        BankAccount.all_accounts[self.account_number] = self
        
        print(f"Account created successfully! Account Number: {self.account_number}")

    def deposit(self, amount):
        if not self.validate_transaction(amount):
            return
        
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print(f"₹{amount} deposited. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if not self.validate_transaction(amount):
            return
        
        if self.balance - amount < 0:
            print("Insufficient balance!")
            return
        
        self.balance -= amount
        self.transactions.append(f"Withdrawn ₹{amount}")
        print(f"₹{amount} withdrawn. New balance: ₹{self.balance}")

    def transfer(self, target_account_number, amount):
        if target_account_number not in BankAccount.all_accounts:
            print("Invalid account number!")
            return
        
        target_account = BankAccount.all_accounts[target_account_number]
        
        if self.balance - amount < 0:
            print("Insufficient balance for transfer!")
            return
        
        self.withdraw(amount)
        target_account.deposit(amount)
        self.transactions.append(f"Transferred ₹{amount} to Account {target_account_number}")
        target_account.transactions.append(f"Received ₹{amount} from Account {self.account_number}")
        print(f"Successfully transferred ₹{amount} to {target_account.name}")
    
    def get_balance(self):
        print(f"Account Balance: ₹{self.balance}")
        return self.balance
    
    def get_transaction_history(self):
        print(f"Transaction History for {self.name} (Account {self.account_number}):")
        for transaction in self.transactions:
            print("-", transaction)
    
    @classmethod
    def get_total_accounts(cls):
        print(f"Total Accounts: {cls.total_accounts}")
        return cls.total_accounts
    
    @staticmethod
    def validate_transaction(amount):
        if amount <= 0 or amount > 50000:
            print("Transaction failed! Amount must be between ₹1 and ₹50,000.")
            return False
        return True

# Creating accounts
account1 = BankAccount("Alice", "Savings", 5000)
account2 = BankAccount("Bob", "Current", 7000)

# Performing transactions
account1.deposit(2000)
account1.withdraw(3000)
account1.transfer(2, 1500)
account1.get_transaction_history()

# Checking total accounts
BankAccount.get_total_accounts()
