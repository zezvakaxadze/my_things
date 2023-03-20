def line_number(file, list_):
    file_ = open(file, "r", encoding="UTF-8")
    x = 0
    z = []

    for i in range(len(list_) - 1):
        for j in range(len(list_) - i - 1):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]

    for line in file_.readlines():
        x += 1
        for i in list_:
            if i == x:
                z.append(line)

    for i in range(len(list_)):
        if i <= len(z)-1:
            print(f"line {list_[i]}# {z[i]}")
        if i > len(z)-1:
            print(f"line {list_[i]}# douse not exist.")


line_number("text.txt", [80, 14, 4])
