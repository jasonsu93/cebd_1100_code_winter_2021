from Assignment_2.BankingAccount import BankAccount

class SavingAccount(BankAccount):
    def withdrawal(self, amount):
        if self.current_balance >= amount:
            self.current_balance -= amount
            print("You withdrew:", amount)
        else:
            print("Insufficient Funds")