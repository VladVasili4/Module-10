"""
Цель задания:
Практически применить знания о механизмах блокировки потоков в Python, используя класс Lock из модуля threading.

Задание:
Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.

Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег. Необходимо
использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.

Пример работы:
def deposit_task(account, amount):
  for _ in range(5):
    account.deposit(amount)

def withdraw_task(account, amount):
  for _ in range(5):
    account.withdraw(amount)
account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

Вывод в консоль:
Deposited 100, new balance is 1100
Deposited 100, new balance is 1200
Deposited 100, new balance is 1300
Deposited 100, new balance is 1400
Deposited 100, new balance is 1500
Withdrew 150, new balance is 1350
Withdrew 150, new balance is 1200
Withdrew 150, new balance is 1050
Withdrew 150, new balance is 900
Withdrew 150, new balance is 750

Примечание:
Используйте класс Lock из модуля threading для блокировки доступа к общему ресурсу.
Ожидается создание двух потоков, один для пополнения счета, другой для снятия денег.
Используйте with (lock object): в начале каждого метода, чтобы использовать блокировку
"""


from threading import Thread, Lock

lock = Lock()

class BankAccount(Thread):
    balance = 1000


    def __init__(self):
        super().__init__()

    def deposit(self, amount):
        self.amount = amount
        with lock:
            self.balance += self.amount
            print(f'Deposited {self.amount}, new balance is {self.balance}')

    def withdraw(self, amount):
        self.amount = amount
        with lock:
            self.balance -= self.amount
            print(f'Withdrew {self.amount}, new balance is {self.balance}')

def deposit_task(account, amount):
    for i in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for i in range(5):
        account.withdraw(amount)


account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()