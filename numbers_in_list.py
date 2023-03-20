data = ["23", 11, 1.4, None, "Georgia", -12, 1.6, 1.2]

x = 0

for i in data:
    int_or_not_int = isinstance(i, int)
    float_or_not_float = isinstance(i, float)
    if int_or_not_int or float_or_not_float:
        x += i

print("Bowl of all nums: ", x)
