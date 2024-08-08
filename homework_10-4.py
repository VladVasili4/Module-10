from threading import Thread
from time import sleep
import random
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None



class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        t = random.randint(3, 11)
        sleep(t)
        print(f'Выполняется поток {self.name} ')


queue = queue.Queue
class Cafe():
    def __init__(self, tables):
        # self.table = Table(number)
        for t in tables:
            self.table = t.number
            print(f'Cтолик в кафе :{self.table}')


    def guest_arrival(self, *guest ):                      #  (прибытие гостей)
        self.guests = guests
        for g in self.guests:
            g.start()
            print(f"{g} сел(-а) за стол номер {self.table}")
        # queue.put()

#
    def discuss_guests(self):                      # (обслужить гостей)
        while not queue.empty:
            for i in guests:
                i.join()
                print(f'Поел: {i}')
            # queue.get()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
print(f'Столики с номерами {tables} ')


# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
print(f'Гости : {guests}')
# for g in guests:
#     g.start()

# for i in guests:
#     i.join()
#     print(f'Поел: {i}')

# Заполнение кафе столами
cafe = Cafe(tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()