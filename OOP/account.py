
        
class Account:
    def __init__(self, account_number, owner_name, balance, overdraft_limit, interest_rate, min_balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.overdraft_limit = overdraft_limit
        self.interest_rate = interest_rate
        self.min_balance = min_balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (self.balance - amount) >= self.min_balance - self.overdraft_limit:
            self.balance -= amount
            return True
        else:
            return False

    def view_account_details(self):
        return f"Account Owner: {self.owner_name}\nBalance: {self.balance}"

    def change_account_owner(self, new_owner_name):
        self.owner_name = new_owner_name

    def account_statement(self):
        for transaction in self.transaction_history:
            print(transaction)

    def set_overdraft_limit(self, new_overdraft_limit):
        self.overdraft_limit = new_overdraft_limit

    def interest_calculation(self):
        interest_amount = (self.balance * self.interest_rate) / 100
        self.balance += interest_amount

    def freeze_account(self):

     def unfreeze_account(self):

      def transaction_history(self):
        return self.transaction_history

    def set_min_balance(self, new_min_balance):
        self.min_balance = new_min_balance

    def transfer_funds(self, recipient_account, amount):
        if (self.balance - amount) >= self.min_balance - self.overdraft_limit:
            recipient_account.deposit(amount)
            self.withdraw(amount)
            return True
        else:
            return False            