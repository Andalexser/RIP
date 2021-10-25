import math

from lab_python_op.Geometric_shape import Goesh
from lab_python_op.Color import Color

class Circle(Goesh):

    def __init__(self, colo, radius):
        self.col = Color()
        self.col = colo
        self.radius = radius

    def area(self):
        return 2 * self.radius * math.pi

    def __repr__(self):
        return 'Круг площадью {} {} цвета с радиусом {}.'.format(self.area(), self.col, self.radius)
