class Account:
    def __init__(self, balance, interest_rate):
        self.balance= balance
        self.withdraw_count= 0
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.withdraw_count += 1




class ChequingAccount(Account):

    def withdraw(self, amount):
        if self.balance - amount < 0:
            # print("Cannot Withdraw")
            self.balance = self.balance - 15
        else:
            super().withdraw(amount)

account1 = ChequingAccount(10, .001)
account1.withdraw(5.000)

print(account1.balance)