import numpy as np


class Matrix:

    def __init__(self, sor, oszlop):
        self.m = sor
        self.n = oszlop
        self.mtx = np.zeros((self.m,self.n))
        self.feltolt()

    def feltolt(self):
        for i in range(self.m):
            for j in range(self.n):
                self.mtx[i, j] = i * j


m1 = Matrix(3,4)
print(m1.mtx)
# m1.feltolt()
# print(m1.mtx)

# m2 = Matrix(5,5)
# print(m2.mtx)