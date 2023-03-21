dit_1 = {'N123': 67, 'N113': 95,
         'N145': 46, 'N234': 32,
         'N156': 89, 'N098': 51}
list_1 = ["N123", "N113", "N145", "N234", "N156", "N098"]

dit_2 = {}

for i in list_1:
    if 100 >= dit_1[i] > 91:
        dit_2[i] = "A"
    elif 90 >= dit_1[i] > 81:
        dit_2[i] = "B"
    elif 80 >= dit_1[i] > 71:
        dit_2[i] = "C"
    elif 70 >= dit_1[i] > 61:
        dit_2[i] = "D"
    elif 60 >= dit_1[i] > 51:
        dit_2[i] = "E"
    elif 50 >= dit_1[i] > 41:
        dit_2[i] = "F"
    else:
        dit_2[i] = "FX"


a = input("შეიყვანეთ სტუდენტის აიდი: ")

while True:
    if a not in dit_2:
        a = input("შეიყვანეთ სტუდენტის აიდი: ")
    else:
        print(dit_2[a])
        a = input("შეიყვანეთ სტუდენტის აიდი: ")

