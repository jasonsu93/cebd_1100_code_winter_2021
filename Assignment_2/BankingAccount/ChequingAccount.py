from Assignment_2.BankingAccount import BankAccount

class ChequingAccount(BankAccount):

    # def withdrawal(self, amount):
    #     if self.current_balance >= amount:
    #         self.current_balance -= amount
    #         print("You withdrew:", amount)
    #     else:
    #         print("Insufficient Funds")



    def withdrawal(self, amount):
        if self.current_balance - amount < 0:
            self.current_balance -= 15
            print("Insufficent Funds")
        else:
            super(ChequingAccount, self).withdrawal(amount)