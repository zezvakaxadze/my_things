
while True:
    try:
        a = input("write number: ")

        a = int(a)
        a = str(a)
        b = ''

        for i in a:
            b += i + " "
        print(b)

    except ValueError:
        print("write integer number")
