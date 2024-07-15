
        
class Account:
    def __init__(self, account_number, account_owner, balance, overdraft, interest, min_balance):
        self.account_number = account_number
        self.account_owner = account_owner
        self.balance = balance
        self.overdraft = overdraft
        self.interest = interest
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (self.balance - amount) >= self.min_balance - self.overdraft:
            self.balance -= amount
            return True
        else:
            return False

    def view_account_details(self):
        return f"Account Owner: {self.owner_name}{self.balance}"

    def change_account_owner(self, new_owner_name):
        self.account_owner = new_owner_name

    def account_statement(self):
        for transaction in self.transaction_history:
            print(transaction)

    def set_overdraft_limit(self, new_overdraft_limit):
        self.overdraft_limit = new_overdraft_limit

    def interest_calculation(self):
        interest = (self.balance * self.interest) / 100
        self.balance += interest

    def freeze_account(self):

        return self.transaction_history

    def set_min_balance(self, new_min_balance):
        self.min_balance = new_min_balance

    def transfer_funds(self, recipient_account, amount):
        if (self.balance - amount) >= self.min_balance - self.overdraft:
            recipient_account.deposit(amount)
            self.withdraw(amount)
            return True
        else:
            return False            