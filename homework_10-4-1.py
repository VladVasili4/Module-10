from threading import Thread, excepthook
from time import sleep
import random
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None
        # for t in tables:
        #     self.table = t.number
        #     print(f'Cтолик в кафе :{self.table}')



class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        i = random.randint(3, 11)
        sleep(i)
        print(f' {self.name} сидит, ест.')
        raise Exception


# queue = queue.Queue
class Cafe():

    def __init__(self, tables, queue):
        super().__init__()
        self.tables = tables                             # Это список объектов "Cтолы"
        print(f'Класс Кафе self.tables : {self.tables}')
        self.que = queue.Queue
        print(f'Класс Кафе изначальный queue (self.q): {self.que}')


    def guest_arrival(self, *guests):                      #  (прибытие гостей)
        self.guests = guests

        for self.t in self.tables:
            print(f'Выбрали столик № (self.t) : {self.t.number}')
            for self.g in self.guests:
                if self.t.guest == None:
              #  try:                    Где-то здесь надо создать исключение, чтобы игнорировать повторный запуск
              #  потока и продолжить уже со следующим потоком (гостем)

                    print(f'Выбрали гостя self.g : {type(self.g)}')
                    self.t.guest = self.g
                    print(f'self.t.guest : {self.t.guest}')
                    print(f"{self.g.name} сел(-а) за стол номер {self.t.number}")



    def discuss_guests(self):                      # (обслужить гостей)
        while not self.que.empty:
            if self.g.is_alive:
                self.g.join()
                print(f'<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)"')
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