import numpy as np

m = int(input("Kerem a sorok szamat:"))
n = int(input("Kerem az oszlopok szamat:"))

mtx = np.zeros((m,n))

print(mtx)

for i in range(mtx.shape[0]):
    for j in range(mtx.shape[1]):
        mtx[i,j] = i * j

print(mtx)