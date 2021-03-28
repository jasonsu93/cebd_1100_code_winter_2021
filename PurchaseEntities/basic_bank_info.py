class BankAccount:

    def __init__(self, balance, chequing, saving):
        self.balance = balance
        self.chequing = chequing
        self.saving = saving



    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient Funds"

    def checkbalance(self):
        return self.balance




