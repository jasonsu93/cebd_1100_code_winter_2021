class BankAccount:

    def __init__(self, balance, interest_rate):
        self.start_balance = balance
        self.current_balance = balance
        self.interest = interest_rate
        # self.deposit = 0
        # self.total_withdrawal = 0



    def deposit(self, amount):
        self.current_balance += amount
        print("Deposit made. Current balance is :" + amount)


    def withdrawal(self, amount):
        self.current_balance -= amount
        print("Withdrawal made. Current balance is :" + amount)

    def interest(self):
        monthly_interest = self.interest / 12
        monthly_interest = self.current_balance * monthly_interest
        self.current_balance += monthly_interest



# chequing = ChequingAccount(0, .05)
# savings = SavingsAccount(0, .05)
#
# deposit_amt = 10
#
# chequing.deposit(deposit_amt)