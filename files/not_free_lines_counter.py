def file_path(file):
    file_ = open(file, "r", encoding="UTF-8")
    x = 0
    for line in file_.readlines():
        if len(line) > 1:
            x += 1
    return x


print(file_path("text.txt"))
