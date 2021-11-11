import random

user_input = int(input("Enter number"))

numbers = []
for i in range(0, user_input + 1):
    numbers.append(i)

print(numbers)
divisor = []
for number in numbers:
    try:
        if user_input % number == 0:
            divisor.append(number)
    except ZeroDivisionError:
        pass

# divisor.sort()
print(divisor)



