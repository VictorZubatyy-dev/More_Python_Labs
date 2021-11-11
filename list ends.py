def user_input():
    numbers = input("Enter some numbers")
    number_list = numbers.split(" ")
    return number_list


def numbers_list(nums):
    new_list = []
    new_list.append(nums[0])
    new_list.append(nums[len(nums) - 1])

    # for index, number in enumerate(nums):
    #     if index == 0:
    #         new_list.append(number)
    #
    #     elif index == len(nums) - 1:
    #         new_list.append(number)

    print(new_list)


number_list = user_input()
numbers_list(number_list)