"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
from typing import List

with open("new_file.txt", "w", encoding='utf-8') as new_file:
    while True:
        input_str = input("Введите текст ")
        new_file.writelines([input_str, "\n"])
        if input_str == '':
            break
