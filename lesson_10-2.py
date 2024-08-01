import requests
from threading import Thread

class Getter(Thread):
    res = []
    def __init__(self, url):
        super().__init__()
        self.the_url = url

    def run(self):                              #  = target
        responce = requests.get(self.the_url)
        resp = responce.json()
        Getter.res.append(resp)             # Почему Getter, а не self ? Мля, и так и так работает...

threds = []
num_of_genre = 10

for i in range(num_of_genre):
    g = Getter('https://binaryjazz.us/wp-json/genrenator/v1/genre/') #https://binaryjazz.us/wp-json/genrenator/v1/story/
    g.start()
    threds.append(g)

for g in threds:
    g.join()
assert num_of_genre == len(Getter.res), 'Какой-то поток заткнулся'
print(Getter.res)




