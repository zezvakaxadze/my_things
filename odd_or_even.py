""" odd or even app """

while True:
    try:
        n = input("write number and i will tell you it's odd or even, for exit write exit: ")
        if n.upper() == "EXIT":
            break
        elif n[0] == "-" and int(n[1:]):
            if int(n) % 2 == 1:
                print(f"{n} is odd")
            elif int(n) % 2 == 0:
                print(f"{n} is even")
        elif n.isdigit():
            if int(n) % 2 == 1:
                print(f"{n} is odd")
            elif int(n) % 2 == 0:
                print(f"{n} is even")
        elif float(n):
            print("write integer number!")
    except ValueError:
        print("write number!!!")
