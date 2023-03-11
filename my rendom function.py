import time

"""random number generator"""


def ulfric_rand(number):
    try:
        r = time.time()
        c = 16807
        m = 2 ** 31 - 1
        random_number = (c * r) % m

        num = random_number % int(number)
        return round(num)
    except ValueError:
        return "number must be integer"


while True:
    a = input("write number for generate random number: ")

    print(ulfric_rand(a))
