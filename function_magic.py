import random


def sorting_hat(full_name):
    if True is not isinstance(full_name, str):
        return None
    else:
        a = ["Gryffindor",
             "Hufflepuff",
             "Ravenclaw",
             "Slytherin"]
        if "Weasley" in full_name:
            return f"Ah! Another Weasley. I know just what to do with you. {a[0]}!"
        else:
            return f"I know just what to do with you. {random.choice(a)}!"


magicians = ["Harry Potter",
             "Ron Weasley",
             "Hermione Granger",
             "Draco Malfoy",
             "Neville Longbottom",
             "Luna Lovegood",
             ]
for i in magicians:
    print(sorting_hat(i))
