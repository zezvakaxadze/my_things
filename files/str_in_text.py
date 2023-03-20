def text_in_line(file, text):
    file_ = open(file, "r", encoding="UTF-8")
    x = 0
    y = 0
    for line in file_.readlines():
        x += 1
        if text in line:
            y += 1
            return x
    if y == 0:
        return None


print(text_in_line("text.txt", "ცოცხალსა"))
