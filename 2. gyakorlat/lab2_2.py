import math


class Circle:

    def __init__(self, r):
        self.r = r

    def get_area(self):
        return self.r ** 2 * math.pi

    def get_perimeter(self):
        return 2 * self.r * math.pi

    def __str__(self):
        return f'Kör sugara: {self.r}\nTerület: {self.get_area()}\nKerület: {self.get_perimeter()}'

circle1 = Circle(4)
print(circle1)