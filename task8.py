class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print("Рисуется фигура")


class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length

    def draw(self):
        print("Рисуется линия")


class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height

    def draw(self):
        print("Рисуется прямоугольник")


class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius

    def draw(self):
        print("Рисуется эллипс")

class Triangle(Figure):
    def draw(self):
        print("Рисуется треугольник")
        
line = Line((10, 20), 100, "red", 50)
rect = Rect((30, 40), 200, "blue", 100)
ellipse = Ellipse((50, 60), 150, "green", 75)
triangle = Triangle((70, 80), 120, "yellow")


figures = [line, rect, ellipse, triangle]

for figure in figures:
    figure.draw()