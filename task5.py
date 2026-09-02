class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

class Kvadrat(Figure):
    pass

figure1 = Figure((10, 20), 100, "red")
print(figure1.coords, figure1.width, figure1.color)