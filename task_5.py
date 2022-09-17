"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

numbers_sum = 0
with open("task_5.txt", "w", encoding='utf-8') as task_5:
    numbers = []
    for i in range(10):
        numbers.append(str(random.randint(0, 100)))
    task_5.write(" ".join(numbers))
with open("task_5.txt", "r", encoding='utf-8') as task_5:
    line = task_5.read()
    line = line.split(' ')
    for number in line:
        numbers_sum += int(number)
    print(numbers_sum)
