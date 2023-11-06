class SavingAccount(object):
    def __init__(self, bank_name, acc_name, acc_id, balance, transaction_history = []):
        self.bank_name = bank_name
        self.acc_name = acc_name
        self.acc_id = acc_id
        self.balance = balance
        self.transaction_history = transaction_history

    def deposit(self, money, person, date):
        self.balance += money
        self.transaction_history.append(["Deposits", money, person, date])

    def withdraw(self, money, person, date):
        if money > self.balance:
            print("Insufficient balance to withdraw.")

        else:
            self.balance -= money
            self.transaction_history.append(["Withdraw", money, person, date])

    def get_balance(self):
        return self.balance
    
    def print_statement(self):
        print(f"Current balance is {self.balance}")
        print(f"Transaction history: \n {self.transaction_history}")

class OverDrawnAccount(SavingAccount):
    def __init__(self, bank_name, acc_name, acc_id, balance, overdrawn_limit, transaction_history=[]):
        super().__init__(bank_name, acc_name, acc_id, balance, transaction_history)
        self.overdrawn_limit = overdrawn_limit

    def withdraw(self, money, person, date):
        if self.balance - money >= -self.overdrawn_limit:
            self.balance -= money
            self.transaction_history.append([f"Withdraw", money, person, date])

        else:
            print("Withdrawal amount exceeds overdrawn limit.")

overdrawn = OverDrawnAccount("Overdrawn", "John", "123456", 100, 500)

overdrawn.deposit(100, "John", "2023-10-06")
overdrawn.withdraw(200, "John", "2023-10-20")
overdrawn.withdraw(600, "John", "2023-10-30")

overdrawn.print_statement()