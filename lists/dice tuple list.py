import random

x = []

for i in range(6):
    x.append((random.randrange(1, 7), random.randrange(1, 7)))

print(x)


for i in range(6-1):
    for j in range(6-i-1):
        if x[j][0] + x[j][1] > x[j+1][0] + x[j+1][1]:
            x[j], x[j+1] = x[j+1], x[j]
print(x)
