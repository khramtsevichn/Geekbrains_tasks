"""
1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки
и сохраните в переменные, затем выведите на экран.
"""
a = 1
print(a)

b = 10
c = b
print(c)

name = input("Имя?")
print(name)

age = int(input("Возраст?"))
print(age)

"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.
"""
time_input = int(input("Введите время в секундах: "))
time_hrs = time_input // 3600
time_mins = (time_input % 3600) // 60
time_secs = (time_input % 3600) % 60
print(f"Time is: {time_hrs}:{time_mins}:{time_secs}")

"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. 
Считаем 3 + 33 + 333 = 369.
"""
n = input("Введите число: ")
sum_n = int(n) + int(n + n) + int(n +n + n)
print(sum_n)

"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл 
while и арифметические операции.
"""
number = int(input('Введите целое положительное число: '))
max_number = 0
while number != 0:
    digit = number % 10
    if digit > max_number:
        max_number = digit
    number = number // 10
print(max_number)

"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает 
фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. 
Выведите соответствующее сообщение.
6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите 
численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
"""
revenue = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
if revenue < costs:
    print('Убыток')
if revenue > costs:
    print('Прибыль')
    profit = revenue - costs
    viability = (profit / revenue) * 100
    viability = round(viability,2)
    print(f'Рентабельность: {viability}%')
    employees = int(input('Введите количество сотрудников '))
    empl_profit = profit / employees
    print(f'Прибыль в расчете на сотрудника равна {empl_profit}')

"""
7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен
 увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня, на который результат спортсмена 
 составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число 
 — номер дня.
"""
result_1 = int(input("Введите результат в первый день: "))
result_final = int(input("Введите желаемый результат: "))
day = 1
while result_1 < result_final:
    result_1 = result_1 + result_1 * 0.1
    day = day + 1
print(f'Вы достигнете цели через {day} дней')

