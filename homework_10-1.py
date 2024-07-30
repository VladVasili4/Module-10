from time import sleep
import requests
from threading import Thread
from datetime import datetime
import io
from pprint import pprint


def wite_words(word_count, *file_name):
    start_ = datetime.now()
    with open(file_name, 'a', encoding = 'UTF-8') as file:
        for line in file:
            for i in range(word_count):
                file.whrite(f'Какое-то слово № {i}')
                sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

wite_words(10, example1.txt)