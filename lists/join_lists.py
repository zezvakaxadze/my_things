# new list must be like this: ["Hello Dear", "Hello Sir", "Bye Dear", "Bye Sir"]
list_1 = ["Hello ", "Bye "]
list_2 = ["Dear", "Sir"]
list_ = []

for i in list_1:
    for j in list_2:
        list_.append(f"{i} {j}")

print(list_)
