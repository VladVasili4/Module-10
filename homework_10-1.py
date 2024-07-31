from time import sleep
from threading import Thread
from datetime import datetime
import io

def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding = 'UTF-8') as file:
        # for line in file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i} \n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


start_ = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
finish_ = datetime.now()
working_time = finish_ - start_
print(f'Работа потоков {working_time} сек.')


start_1 = datetime.now()
thr1 = Thread(target=wite_words, args = (10, 'example5.txt'))
thr2 = Thread(target=wite_words, args = (30, 'example6.txt'))
thr3 = Thread(target=wite_words, args = (200, 'example7.txt'))
thr4 = Thread(target=wite_words, args = (100, 'example8.txt'))

thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()

finish_1 = datetime.now()
working_time1 = finish_1 - start_1
print(f'Работа потоков {working_time1} сек.')
