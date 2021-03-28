from Assignment_2.BankingAccount import BankAccount
# from Assignment_2.BankingAccount import SavingAccount

if __name__ == "__main__":
    while True:
        print("1: Savings")
        print("2: Chequing")
        print("Q: Quit")
        menu1 = input("Enter a choice >>>")

        if menu1 == "1":
            while True:
                print("1: Deposit")
                print("2: Withdrawal")
                print("Q: Back")
                menu2 = input("Enter a choice >>>")
                if menu2 == "1":
                    n = int(input("How much would you like to deposit? >>>"))
                if menu2 == "2":
                    n = int(input("How much would you like to withdraw? >>>"))
                elif menu2 == "Q" or menu2 == "q":
                    print("Going to Previous Menu")
                    break
        if menu1 == "2":
             while True:
                print("1: Deposit")
                print("2: Withdrawal")
                print("Q: Back")
                menu3 = input("Enter a choice >>>")
                if menu3 == "1":
                    n = int(input("How much would you like to deposit? >>>"))
                elif menu3 == "Q" or menu3 == "q":
                    print("Going to Previous Menu")
                    break
        if menu1 == "Q" or menu1 == "q":
            print("Existing Program")
            break
