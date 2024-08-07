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
        self.name = name


    def run(self):
        t = random.randint(3, 11)
        sleep(t)



class Cafe:
    queue = queue.Queue
    tables = [Table(number) for number in range(1, 6)]

    def guest_arrival(self):                      #  (прибытие гостей)

        pass

    def discuss_guests(self):                      # (обслужить гостей)


        pass