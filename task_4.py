"""
4. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

income_sum = 0
with open("task_4.txt", "r", encoding='utf-8') as task_4:
    lines = task_4.readlines()
    for line in lines:
        line = line.split(' ')
        line[1] = float(line[1])
        if line[1] < 20000.00:
            print(line[0])
        income_sum += line[1]
    average_income = income_sum / len(lines)
    print(round(average_income, 2))
