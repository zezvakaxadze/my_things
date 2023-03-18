# if only one number is a negative number print False
# in another situations print True heh

a = input("write number: ")
b = input("write number: ")

print((a.isdigit and a[0] != '-' and b[0] == "-" and b[1:].isdigit()) or (a[0] == '-' and b.isdigit() and b[0] != "-"
                                                                          and a[1:].isdigit()))
