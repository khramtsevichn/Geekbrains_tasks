'''2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число
см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.'''


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def coverage(self, mass, height):
        return self._length * self._width * mass * height


road = Road(length=1000, width=20)

print(road.coverage(mass=200, height=2))
print(road.coverage(mass=200, height=4))
