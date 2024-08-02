from threading import Thread, Lock

lock = Lock()
class BankAccount:
    bankAcc = 1000

    def __init__(self, accaunt):
        self.accaunt = accaunt


    def deposit_task(self, account, amount):
        self.amount = amount
        global bankAcc
        for i in range(5):
            with lock:
                bankAcc += self.amount


        account.deposit(amount)

    def withdraw_task(self, account, amount):
        for _ in range(5):
            account.withdraw(amount)


account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()