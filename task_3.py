"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
rus_words = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
task_3_new_file = []
with open("task_3.txt", "r", encoding ='utf-8') as task_3:
    content = task_3.readlines()
    for line in content:
        line = line.split(' ')
        task_3_new_file.append(f'{rus_words[line[0]]} {line[1]} {line[2]}')
with open("task_3_new.txt", "w", encoding='utf-8') as task_3_new:
    task_3_new.writelines(task_3_new_file)