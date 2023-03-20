import random

top_10_dishes = ["ბელგიური ვაფლი ნაყინით",
                 "ტირამისუ",
                 "სტეიკი და ფრი",
                 "იტალიური სენდვიჩი",
                 "გირო",
                 "ბერძნული სალათი",
                 "მოცარელას ჩხირები",
                 "ომლეტი",
                 "ქათმის ბურგერი და ფრი",
                 "პასტა",
                 ]

seven_days = []


for i in range(7):
    c = random.choice(top_10_dishes)
    seven_days.append(c)
    top_10_dishes.remove(c)

for i in range(7):
    print(f"დღე {i + 1}# {seven_days[i]}")




