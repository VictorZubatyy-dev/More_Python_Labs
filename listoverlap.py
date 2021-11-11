import random

random1 = random.sample(range(1,50), 7)
print(random1)
random2 = random.sample(range(1,30), 7)
print(random2)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] #11
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] #13

# a_count = len(a)
# b_count = len(b)

#
# print(a_count)
# print(b_count)

common = []


for index, number in enumerate(random1):
    for i, num in enumerate(random2):
        if random1[index] == random2[i] and number not in common:
            common.append(number)

print(common)
