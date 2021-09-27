class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return self.__class__(self.real, -self.imag)

    def argz(self):
        import math
        return math.atan(self.imag / self.real)

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5

    def __str__(self):
        return "{} + {}j".format(self.real, self.imag)

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            self.real += other.real
            self.imag += other.imag
        elif isinstance(other, int) or isinstance(other, float):
            self.real += other
        return self

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            self.real -= other.real
            self.imag -= other.imag
        elif isinstance(other, int) or isinstance(other, float):
            self.real -= other
        return self

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            self.real = (self.real * other.real) - (self.imag * other.imag)
            self.imag = (self.real * other.imag) + (other.real * self.imag)
        if isinstance(other, int) or isinstance(other, float):
            self.real *= other
            self.imag *= other
        return self

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return (self.real == other.real) and (self.imag == other.imag)
        else:
            return 'Nem osszehasonlithato'

    def __ne__(self, other):
        if isinstance(other, ComplexNumber):
            return (self.real != other.real) or (self.imag != other.imag)
        else:
            return 'Nem osszehasonlithato'