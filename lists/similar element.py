def similar(list1, list2):
    b = False
    for i in list1:
        if i in list2:
            b = True
    return b


print(similar([1, 2, 3], [2, 3]))
