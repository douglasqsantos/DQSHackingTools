# Python program creating
# thread using multiprocessing
# module

import multiprocessing
import time

def func(number):
    for i in range(1, 10):
        time.sleep(0.01)
        print('Processing ' + str(number) + ': prints ' + str(number*i))

for i in range(0, 3):
    process = multiprocessing.Process(target=func, args=(i,))
    process.start()
