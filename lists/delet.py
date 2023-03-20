numbers = [5, 20, 15, 20, 25, 50, 20]
print(f"befor remove: {numbers}")
for i in numbers:
    if i == 20:
        numbers.remove(i)
print(f"after remove: {numbers}")
