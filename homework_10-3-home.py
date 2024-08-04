from threading import Thread, Lock

lock = Lock()
class BankAccount:
    bankAcc = 1000

    def __init__(self,account):
        super().__init__()
    #     self.account = account
    #     # self.amount = amount


    def deposit_task(self, account, amount):
        self.account = account
        self.amount = amount
        global bankAcc
        for i in range(5):
            with lock:
                bankAcc += self.amount


        # account.deposit(amount)

    def withdraw_task(self, account, amount):
        self.account = account
        self.amount = amount
        global bankAcc
        for i in range(5):
            with lock:
                bankAcc -= self.amount
            account.withdraw(self.amount)


account = BankAccount(123456789)

deposit_thread = Thread(target=BankAccount.deposit_task, args=(account, 100))
withdraw_thread = Thread(target=BankAccount.withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()