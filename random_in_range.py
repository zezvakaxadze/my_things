import random
while True:
    a = int(input("write number: "))
    b = int(input("write number: "))

    if a > b:
        print(random.randrange(b, a))
    else:
        print(random.randrange(a, b))

