class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return f'A: {self.a}\nB: {self.b}\nTerület: {self.get_area()}\nKerület: {self.get_perimeter()}'

tegla1 = Rectangle(3,4)
print(tegla1)

