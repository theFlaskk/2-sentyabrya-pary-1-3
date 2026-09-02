class Graph:
    def __init__(self, _x, _y, scale):
        self.x = _x
        self.y = _y
        self.scale = scale
    
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def change_scale(self, factor):
        self.scale *= factor
graph1 = Graph(0, 0, 1)
graph2 = Graph(10, 10, 2)
graph3 = Graph(5, 5, 1)

graph1.move(1, 1)
graph2.change_scale(factor=0.5)

print(graph1.x, graph1.y, graph1.scale)
print(graph2.x, graph2.y, graph2.scale)
print(graph3.x, graph3.y, graph3.scale)