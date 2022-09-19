'''
3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение
(__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек
этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку:
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку:
*****\n*****\n*****.
'''

class Cage:
    def __init__(self, n):
        self.cells_num = n

    def __add__(self, other):
        if type(other) == Cage:
            return Cage(self.cells_num + other.cells_num)

        else:
            raise ValueError("We can add only Cage to Cage")

    def __sub__(self, other):
        if type(other) == Cage:
            if self.cells_num > other.cells_num:
                return Cage(self.cells_num - other.cells_num)
            else:
                raise ValueError("Error!")

        else:
            raise ValueError("We can sub only Cage to Cage")

    def __mul__(self, other):
        if type(other) == Cage:
            return Cage(self.cells_num * other.cells_num)

        else:
            raise ValueError("We can mul only Cage to Cage")

    def __truediv__(self, other):
        if type(other) == Cage:
            return Cage(int(round(self.cells_num / other.cells_num, 0)))

        else:
            raise ValueError("We can truediv only Cage to Cage")


    @staticmethod
    def make_order(cage, length):
        num = cage.cells_num
        num_of_complete_rows = num // length
        last_row = num - num_of_complete_rows * length

        result = ""
        for i in range(num_of_complete_rows):
            result += ("*" * length) + "\n"

        result += '*' * last_row
        print(result)






cage1 = Cage(100)
cage2 = Cage(200)

cage3 = cage1 + cage2
print(cage3.cells_num)

cage4 = cage2 - cage1
print(cage4.cells_num)


cage5 = cage2 * cage1
print(cage5.cells_num)


cage6 = cage2 / cage1
print(cage6.cells_num)

cage7 = cage2 / Cage(1000)
print(cage7.cells_num)

Cage.make_order(cage1, 9)