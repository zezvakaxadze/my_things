a = input("write sting: ")

x = round(len(a) / 2)
b = 1
for i in range(x):
    if a[i] == a[-(i+1)]:
        b = 1
    else:
        b = 0
if b == 1:
    print("it's polindrome")
else:
    print("it's not polindrom")