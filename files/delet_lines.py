def function(file, text):
    file_ = open(file, "r", encoding="UTF-8")
    file_1 = open("text1.txt", "w", encoding="UTF-8")
    for i in file_.readlines():
        if text in i:
            continue
        else:
            file_1.writelines(i)


function("text.txt", "კარგ")

