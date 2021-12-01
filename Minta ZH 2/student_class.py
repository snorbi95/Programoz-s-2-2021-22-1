class NeptunCodeFormatException(Exception):

    def __init__(self, neptun):
        self.neptun = neptun

    def __str__(self):
        return f'A {self.neptun} kód hibás!'

class Student:

    def __init__(self, name, neptun, email):
        self.name = name
        self.neptun = neptun
        self.email = email
        self.marks = dict()

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.neptun == other.neptun

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.neptun < other.neptun

    def __le__(self, other):
        if isinstance(other, Student):
            return self.neptun <= other.neptun

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.neptun >= other.neptun

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.neptun > other.neptun

    def __str__(self):
        return f'{self.name},{self.neptun},{self.email}'