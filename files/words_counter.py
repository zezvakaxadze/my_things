file_ = open("text.txt", "r", encoding="UTF-8")

file_line = file_.read().split()

print(len(file_line))
