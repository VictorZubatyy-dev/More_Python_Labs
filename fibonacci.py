def user_input():
    no = int(input("How many fibonacci numbers?"))
    return no


def fibonacci(count):
    number_list = []
    global fibonacci_list
    fibonacci_list = []
    for i in range(0, count * 10000):
        number_list.append(i)

    # print(number_list)

    for index, number in enumerate(number_list):
        if index == 0 or index == 1:
            fibonacci_list.append(number)
            count -= 1
            if count == 0:
                print(fibonacci_list)
                break;
        else:
            return fibonacci_list_add(fibonacci_list, count)


def fibonacci_list_add(fibo_list, counter):
    for i, num in enumerate(fibonacci_list):
        fibonacci_number = fibonacci_list[i] + fibonacci_list[i + 1]
        fibonacci_list.append(fibonacci_number)
        counter -= 1

        if counter == 0:
            print(fibonacci_list)
            break;


numbers = user_input()
fibonacci(numbers)

