a = input("write string: ")
b = input("write symbol/symbols for operation: ")

if b in a:
    print(f"index number: {a.index(b)}")
else:
    print("can't finde a symbol")
