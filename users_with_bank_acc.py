class User:

    # bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self

class BankAccount:

    def __init__(self):
        self.int_rate = 0.01
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self

jack = User("Jack Smith", "jack@gmail.com")
account_1 = BankAccount()
jack.account = account_1
jack.make_deposit(100).make_deposit(200).make_deposit(200).make_withdrawal(50).display_user_balance()