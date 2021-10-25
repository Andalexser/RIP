from lab_python_op.Rectangle import Rectangle
from lab_python_op.Color import Color

class Square(Rectangle):

    def __init__(self, colo, side):
        self.col = Color()
        self.col = colo
        self.side = side

    def area(self):
        return self.side * self.side

    def __repr__(self):
        return 'Квадрат площадью {} {} цвета со стороной {}.'.format(self.area(), self.col, self.side)