x = input("write number: ")
a = 0
b = len(x)
c = 0

for i in x:
    c += 1
    if b == c and a < int(i):
        print(True)
    elif a < int(i):
        a = int(i)
        continue
    elif a > int(i):
        print(False)
        break
