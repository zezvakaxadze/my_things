
a = input("write file location: ")

file_ = open(a, "r", encoding="UTF-8")

x = 0
for i in file_.readlines():
    x += 1
    print(f"{x}. {i}")
