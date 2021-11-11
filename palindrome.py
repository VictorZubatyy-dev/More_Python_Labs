user_input = input("Enter a number or word")

#lists are only used if u wanna modify ur string
# string = user_input
# list = []
#
# for c in string:
#     list.append(c)
#
# print(list)


count = len(user_input)
print(count)

for index, number in enumerate(user_input):
    if user_input[index] == user_input[count - 1]:
        count -= 1
        print("Could be a palindrome")
        if count == 0:
            print("palindrome")
            break;
        # if number.index() == number-number.index():
        #     palindrome()
    else:
        print("not a palindrome")
        break;




