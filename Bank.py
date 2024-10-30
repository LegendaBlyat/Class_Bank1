
class BankAccount:
    account_number = None
    balance = None
    account_holder = None
    transaction_history = []

    def operation(self,account_number,balance,account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder
        self.transaction_history = []


    def deposit(self, amount): #Пополнение
        self.balance = self.balance + amount
        print('Успешно попоплнено, ваш баланс: ', amount)
        self.transaction_history.append(f"+{amount}")


    def withdraw(self, amount): #Снятие
        if amount <= self.balance:
            self.balance = self.balance - amount
            print('Операция успешно выполнена, ваш баланс: ', self.balance)
        else:
            print('Недостаточно средств на счёте')
        self.transaction_history.append(f"-{amount}")


    def display_balance(self):
        print('Ваш баланас: ', self.balance)

    def get_transaction_history(self, ):
        print(self.transaction_history)


Bob = BankAccount()
Bob.operation(account_holder='Bob', balance=0, account_number='123456789')

# Bob.deposit(0)
# Bob.withdraw(0)
# Bob.display_balance()
# Bob.get_transaction_history()

Mario = BankAccount()
Mario.operation(account_holder='Mario', balance=0, account_number='987654321')

Mario.deposit(100)
Mario.withdraw(50)
Mario.display_balance()
Mario.get_transaction_history()







