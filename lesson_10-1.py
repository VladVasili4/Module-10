import requests
from threading import Thread
from datetime import datetime
start_ = datetime.now()
the_url = 'https://binaryjazz.us/wp-json/genrenator/v1/story/'
# https://binaryjazz.us/wp-json/genrenator/v1/genre/
res = []

# for i in range(10):
#     responce = requests.get(the_url)
#     resp = responce.json()
#     res.append(resp)

# print(res, sep='\n')
# finish_ = datetime.now()
# time_ = finish_ - start_
# print(f'Время работы программы:{time_}')

def func(url):
    responce = requests.get(the_url)
    resp = responce.json()
    res.append(resp)


thread1 = Thread(target = func, args = [the_url])
thread2 = Thread(target = func, args = [the_url])
thread3 = Thread(target = func, args = [the_url])

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print(res, sep='\n')
finish_ = datetime.now()
time_ = finish_ - start_
print(f'Время работы программы:{time_}')
