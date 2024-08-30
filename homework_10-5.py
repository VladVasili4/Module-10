import multiprocessing
import io
import os
import sys
from datetime import datetime


def read_info(name):
    all_data = []
    my_folder = os.path.dirname(os.path.abspath(sys.argv[0]))
    folder2 = 'files_10_5'
    name_of_file = os.path.join(my_folder, folder2, name)
    with open (name_of_file, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break
    print(all_data)

start1 = datetime.now()

for i in range(1, 5):
    name = f'file {i}.txt'
    print(name)
    read_info(name)

end1 = datetime.now()
time_of_line_function = end1 - start1
print(f'Время работы линейного вызова : {time_of_line_function}')



if __name__ == '__main__':

    start2 = datetime.now()

    files = []
    for i in range(1, 5):
        name = f'file {i}.txt'
        files.append(name)
    with multiprocessing.Pool(processes=4) as pool:


        # print(files)
        pool.map(read_info, files)

    end2 = datetime.now()
    time_of_multiprocessing = end2 - start2
    print(f'Время работы мультипроцесса : {time_of_multiprocessing}')




# print(folder3)
# files = os.listdir('directory')
# print(f'Путь к файлу : {sys.argv[0]}')
# print(f'Путь к папке : {os.path.dirname(os.path.abspath(sys.argv[0]))}')
# print(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0]))))


if __name__ == '__main__':
    pass