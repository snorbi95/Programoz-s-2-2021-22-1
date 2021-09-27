class Triangle:

    def __init__(self, p1, p2, p3 = 'Nem definialt'):
        if p3 == 'Nem definialt':
            self.a = p1
            self.m = p2
        else:
            self.a = p1
            self.b = p2
            self.c = p3

    def get_area(self):
        if hasattr(self, 'c'):
            s = (self.a + self.b + self.c) / 2
            return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        else:
            return self.a * self.m / 2

    def get_perimeter(self):
        if hasattr(self, 'b'):
            return self.a + self.b + self.c
        else:
            return 'Nem szamolhato kerulet'

    def __str__(self):
        if hasattr(self, 'c'):
            return f'A: {self.a}, B: {self.b}, C: {self.c}'
        else:
            return f'A: {self.a}, M: {self.m}'

    def __add__(self, other):
        if isinstance(other, Triangle):
            return self.get_area() + other.get_area()
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_area() + other

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Triangle):
            return self.get_area() - other.get_area()
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_area() - other

    def __eq__(self, other):
        if isinstance(other, Triangle):
            return self.get_area() == other.get_area()
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_area() == other

    def __ne__(self, other):
        if isinstance(other, Triangle):
            return self.get_area() != other.get_area()
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_area() != other

    def __lt__(self, other):
        if isinstance(other, Triangle):
            return self.get_area() < other.get_area()
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_area() < other

    def __gt__(self, other):
        if isinstance(other, Triangle):
            return self.get_area() > other.get_area()
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_area() > other

    def __ge__(self, other):
        if isinstance(other, Triangle):
            return self.get_area() >= other.get_area()
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_area() >= other

    def __le__(self, other):
        if isinstance(other, Triangle):
            return self.get_area() <= other.get_area()
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_area() <= other



tri1 = Triangle(3,4,5)
tri2 = Triangle(3,4,5)
tri3 = Triangle(10,6)

# print(tri1.get_area(), tri2.get_area())
print(tri1 <= tri2)

# print(tri1.get_area())
# print(tri2.get_perimeter())
# print(tri3)

# print(tri1 == tri1)



