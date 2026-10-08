class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, new_account_number):
        self.__account_number = new_account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("The balance must not be a negative number.")


a1 = BankAccount(12345, 1000)

print("Account 1")
print("Account Number:", a1.account_number)
print("Balance: {:.2f}".format(a1.balance))

print("\nUpdate balance to -100")
a1.balance = -100

print("Account Number:", a1.account_number)
print("Balance: {:.2f}".format(a1.balance))