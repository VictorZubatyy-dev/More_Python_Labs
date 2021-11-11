def get_integer():
    return int(input("Give me a number"))


def check_integer(num):
    numbers = []
    for i in range(1, num + 1):
        numbers.append(i)

    print(numbers)
    divisor = []
    for number in numbers:
        if num % number == 0:
            divisor.append(number)

    if len(divisor) <= 1 or len(divisor) > 2:
        print("not a prime")

    else:
        print("prime")

    #divisor.sort()
    # print(divisor)


number_input = get_integer()
check_integer(number_input)