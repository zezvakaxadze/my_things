x = input("write integer number: ")

if "." not in x:
    if len(x) >= 2:
        if x[1].isdigit() and x.isdigit():
            print("it's valid")
        elif x[0] == "-" or x[0] == "+" and x[1:].isdigit():
            print("it's valid")
        else:
            print("it's not valid")
    else:
        if x.isdigit():
            print("it's valid")
        else:
            print("it's not valid")
else:
    print("it's not valid")
