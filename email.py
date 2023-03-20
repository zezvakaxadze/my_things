first_name = input("first name: ")

while not first_name.isascii():
    first_name = input("english plz: ")

last_name = input("last name: ")

while not last_name.isascii():
    first_name = input("english plz: ")

while True:
    if first_name.isascii() and last_name.isascii():
        x = len(first_name)
        y = len(last_name)
        b = 1
        for i in range(x):
            if first_name[i].isdigit():
                b = 0
                break
        for i in range(y):
            if last_name[i].isdigit():
                b = 0
                break
        if b == 1:
            print(f"{first_name}.{last_name}@gmail.com")
            break
        else:
            print("write whis alpabet")
            first_name = input("first name: ")
            last_name = input("last name: ")






