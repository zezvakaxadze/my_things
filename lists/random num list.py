# in list must be 10 random elements. 1000 > number > 100
import random

list_ = []

for i in range(10):
    list_.append(random.randrange(100, 1000))

print(list_)
