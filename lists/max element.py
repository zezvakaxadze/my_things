# soft must work without max()

numbers = [5, 20, 15, 20, 25, 50, 20]

x = 0

for i in numbers:
    if i > x:
        x = i

print(x)