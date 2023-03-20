x = 5

for i in range(6):
    if i == 0:
        continue
    print(" " * x, "*" * i + "*" * (i - 1))
    x -= 1
