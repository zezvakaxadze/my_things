a = float(input("write a: "))
b = float(input("write b: "))

if a == 0 and b == 0:
    print('solutions are infinite')
elif a == 0 and b != 0:
    print("don't have solution")
else:
    print(b/a)
