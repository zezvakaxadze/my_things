import math

a = input("write string: ")

x = math.ceil(len(a) / 2)

print(f"{a[x:]}{a[0:x]}")
