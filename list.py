a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list = []

for number in a:
    if number % 2 == 0:
        list.append(number)

print(list)