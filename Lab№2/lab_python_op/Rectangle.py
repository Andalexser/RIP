from lab_python_op.Geometric_shape import Goesh
from lab_python_op.Color import Color

class Rectangle(Goesh):

    def __init__(self, colo, length, width):
        self.col = Color()
        self.col = colo
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __repr__(self):
        return 'Прямоугольник площадью {}, {} цвета с длиной {}. и шириной {}.'.format(
            self.area(),
            self.col,
            self.length,
            self.width
        )
