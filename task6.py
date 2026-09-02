class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color


class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length


class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height


class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius


line = Line((10, 20), 100, "red", 50)
rect = Rect((30, 40), 200, "blue", 100)
ellipse = Ellipse((50, 60), 150, "green", 75)


print("Line:")
print(line.coords, line.width, line.color, line.length)

print("Rect:")
print(rect.coords, rect.width, rect.color, rect.height)

print("Ellipse:")
print(ellipse.coords, ellipse.width, ellipse.color, ellipse.radius)