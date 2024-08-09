from threading import Thread
from time import sleep
import random
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = False
        # for t in tables:
        #     self.table = t.number
        #     print(f'Cтолик в кафе :{self.table}')



class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        t = random.randint(3, 11)
        sleep(t)
        print(f' {self.name} сидит, ест.')


queue = queue.Queue
class Cafe():

    def __init__(self, tables, queue):
        self.tables = tables
        self.queue  = queue


    def guest_arrival(self, *guests ):                      #  (прибытие гостей)
        self.guests = guests
        for t in self.tables:
            if t.guest == False:
                for g in self.guests:
                    g.start()
                    t.guest = g
                    print(f"{g.name} сел(-а) за стол номер {t}")
                else: queue.put(item=self.g)

#
    def discuss_guests(self):                      # (обслужить гостей)
        while not queue.empty:
            # if self.
            for i in guests:
                i.join()
                print(f'Поел: {i}')
            self.queue.get(i)

# Создание столов
tables = [Table(number) for number in range(1, 6)]          # Это генератор списка!!!
print(f'Столики с номерами {tables} ')


# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]             # Это генератор списка!!!
print(f'Гости : {guests}')
# for g in guests:
#     g.start()

# for i in guests:
#     i.join()
#     print(f'Поел: {i}')

# Заполнение кафе столами
cafe = Cafe(tables, queue)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()