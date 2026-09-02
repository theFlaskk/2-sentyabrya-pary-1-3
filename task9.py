import math


class Figure:
    def __init__(self, coords):
        self.__coords = coords

    def get_coords(self):
        return self.__coords

    def set_coords(self, coords):
        self.__coords = coords


class Circle(Figure):
    def __init__(self, coords, radius):
        super().__init__(coords)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Square(Figure):
    def __init__(self, coords, side):
        super().__init__(coords)
        self.side = side

    def calculate_area(self):
        return self.side ** 2


figures = [
    Circle((10, 20), 5),
    Square((30, 40), 4),
    Circle((50, 60), 3),
    Square((70, 80), 6),
    Circle((90, 100), 2)
]


total_area = 0

for figure in figures:
    total_area += figure.calculate_area()

print("Общая площадь:", total_area)