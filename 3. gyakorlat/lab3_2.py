import math


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            #return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):
            self.x += other
            self.y += other
            #return Vector(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
            #return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, int):
            self.x -= other
            self.y -= other
            #return Vector(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            self.x *= other.x
            self.y *= other.y
            #return Vector(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            self.x *= other
            self.y *= other
            #return Vector(self.x * other, self.y + other)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.__abs__() == other.__abs__()
        else:
            return 'Nem osszehasonlithato'

    def __ne__(self, other):
        if isinstance(other, Vector):
            return self.__abs__() != other.__abs__()
        else:
            return 'Nem osszehasonlithato'

    def __gt__(self, other):
        if isinstance(other, Vector):
            return self.__abs__() > other.__abs__()
        else:
            return 'Nem osszehasonlithato'

    def __lt__(self, other):
        if isinstance(other, Vector):
            return self.__abs__() < other.__abs__()
        else:
            return 'Nem osszehasonlithato'

    def __ge__(self, other):
        if isinstance(other, Vector):
            return self.__abs__() >= other.__abs__()
        else:
            return 'Nem osszehasonlithato'

    def __le__(self, other):
        if isinstance(other, Vector):
            return self.__abs__() <= other.__abs__()
        else:
            return 'Nem osszehasonlithato'

vec1 = Vector(2,3)
vec2 = Vector(3,2)
print(vec1 + vec2)