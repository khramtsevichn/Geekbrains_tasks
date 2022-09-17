"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""


def get_number(value: str):
    number = value.find("\n")
    if number == -1:
        return int(value)
    return int(value[:number])
import json

firms = dict()
with open("task_7.txt", "r", encoding='utf-8') as task_7:
    lines = task_7.readlines()
    for line in lines:
        values = line.split(' ')
        name, owner, income, costs = values[0], values[1], int(values[2]), get_number(values[3])
        profit = income - costs
        firms[name] = profit

    result = list(filter(lambda a: a >= 0, firms.values()))
    arr = [firms, {"average_profit": sum(result) / len(result)}]

with open("task_7_result.json", "w", encoding='utf-8') as task_7:
    json.dump(arr, task_7)
