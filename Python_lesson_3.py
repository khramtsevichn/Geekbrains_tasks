'''1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.'''


def division_operation(arg1, arg2):
    if arg2 == 0:
        print('Деление на ноль невозможно')
        raise ValueError()
    return arg1 / arg2


try:
    number1 = float(input(f'Введите число 1: '))
    number2 = float(input(f'Введите число 2: '))
except:
    print('Неверный тип данных. Пожалуйста, введите число.')
else:
    print(division_operation(number1, number2))

'''2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год 
рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить 
вывод данных о пользователе одной строкой.'''


def user_data(name, surname, birth_year, residence_city, email, phone_number):
    print(
        f'имя: {name}, фамилия: {surname}, год рождения: {birth_year}, город проживания: {residence_city}, email: {email},'
        f'телефон: {phone_number}')


user_data(phone_number='+375295784692', email='user@mail.ru', residence_city='Минск', birth_year=1980, surname='Иванов',
          name='Иван')

'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух 
аргументов.'''


def my_func(argument1, argument2, argument3):
    arr = [argument1, argument2, argument3]
    max_1 = max(arr)
    arr.remove(max_1)
    max_2 = max(arr)
    return max_1 + max_2


print(f'Сумма наибольших двух аргументов равна {my_func(1, 5, 10)}')

'''4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение числа x 
в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной функции 
возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более
сложная реализация без оператора **, предусматривающая использование цикла.'''


def my_func(x, y):
    if type(x) != float or x <= 0:
        raise ValueError()
    if type(y) != int or y >= 0:
        raise ValueError()
    return x ** y


def my_func2(x, y):
    if type(x) != float or x <= 0:
        raise ValueError()
    if type(y) != int or y >= 0:
        raise ValueError()
    x_buf = x
    for el in range(abs(y)):
        x = x / x_buf
    return x / x_buf


x = 5.0
y = -1
try:
    print(f'Результат возведения числа {x} в степень {y} равен {my_func(x, y)}')
    print(f'Результат возведения числа {x} в степень {y} равен {my_func2(x, y)}')
except:
    print('Неверный тип данных')

'''5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма
 чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел
  будет добавляться к уже подсчитанной сумме.
   Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён 
   после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить 
   программу.'''


def my_func():
    total = 0
    while True:
        numbers = input('Введите строку чисел через пробел ').split()
        for el in numbers:
            if el == '*':
                print(total)
                return
            total = total + int(el)
        print(total)


my_func()

'''6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной 
первой буквой. Например, print(int_func(‘text’)) -> Text.
7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово 
состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с 
заглавной буквы. Используйте написанную ранее функцию int_func().'''

words = input('Введите слова латинскими буквами через пробел ').split()


def words_function(words: list):
    for el in range(len(words)):
        words[el] = words[el].capitalize()
    print(' '.join(words))


words_function(words)
