import numpy as np

s = {14, 87, 33, 44, 47, 99, 4, 22}

average = sum(s) / len(s)

res = set()

for item in s:
    if item > average:
        res.add(item)

print(f'Átlag: {average}\n{res}')