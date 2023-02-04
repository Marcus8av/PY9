from isOdd import isOdd  # проверка числа на четность

print(isOdd(1))  
print(isOdd(4)) 


from progress.bar import Bar # имитация процесса чтения данных
import time

bar = Bar('Progressing', max=20)
for i in range(20):
    time.sleep(1)
    bar.next()
bar.finish()


import emoji # как вывести смайлы

print(emoji.emojize('Python is :thumbs_up:'))

import matplotlib.pyplot as plt # как нарисовать функции
import numpy as np

list = [1, 2, 3, 2, 7, 9, 4]
plt.plot(list)
plt.show()