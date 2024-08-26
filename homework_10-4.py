from threading import Thread, excepthook
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
        i = random.randint(3, 11)
        sleep(i)
        print(f' {self.name} сидит, ест.')


class Cafe():

    def __init__(self, tables, queue):
        super().__init__()
        self.tables = tables                             # Это список объектов "Cтолы"
        self.que = queue.Queue()



    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest = guest
                    break
            else:
                print(f'{guest.name} в очереди')
                self.que.put(guest)


    def discuss_guests(self):                      # (обслужить гостей)
        while not self.que.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if not table.guest is None and table.guest.is_alive:
                    table.guest.join()
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)"')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен.')
                if not self.que.empty() and table.guest is None:
                    table.guest = self.que.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()





                # for i in guests:
                #     i.join()
                # self.queue.get(i)
                # print(f'Поел: {i}')


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