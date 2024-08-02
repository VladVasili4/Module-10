from threading import Thread, Lock

x = 0
lock = Lock()
# def thread_task():
#     global x
#     for i in range(10_000_000):
#         lock.acquire()
#         x = x + 1
#         lock.release()

#         Другой вариант, абсолютно идентичный
def thread_task():
    global x
    for i in range(10_000_000):
        with lock:
          x = x + 1

def main():
    global x
    x = 0
    t1 = Thread(target=thread_task)
    t2 = Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


for i in range(3):
    main()
    print(x)

 # """ Без блокировок этот пример ничего не показывает, т.к. у меня Python 3.12
 #  А в версии более 3,10 (x=x+1) операция атомарная"""


