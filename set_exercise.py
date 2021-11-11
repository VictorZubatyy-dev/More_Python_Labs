#
# Set exercises
# author: B. Schoen-Phelan
# date: Oct 2021
# resources: Python documentation
#

# create two containers that hold the same data
# one is a list and one is a set
# to try the example comment out one or the other
# my_alphabet = ['a', 'b', 'c', 'd', 'e']
my_alphabet = {'a', 'b', 'c', 'd', 'e'}

# this works for both containers, sets and lists:
# for character in my_alphabet:
#     print(character)

# get counter as well
# works for both
#
# for index, character in enumerate(my_alphabet):
#     print("index %d: %d"%(index, character))

# this only works for lists
# if you run this for a set, you will get an error:
# TypeError: 'set' object is not subscriptable
# you get this error for sets because sets are not
# indexed
#
# index = 0
# while index < len(my_alphabet):
#     print(my_alphabet[index])
#     index += 1

# run this a few times
# and note how the letters in the index positions
# change in each run. This is because you cannot
# rely on the order in which things are stored in
# a set.
my_iterator = enumerate(my_alphabet)

# for index in my_iterator:
#     print(index)

#
# if you want to implement the same thing using a
# while loop, then you need to call the
# dunder method __next__ of the iterator to retrieve
# the next element in the list.
# Like with the for loop, if you run this multiple times
# you see how the order of the elements is different.
#
index = 0
end = len(my_alphabet)

while index < end:
    print(my_iterator.__next__())
    index += 1


# the set data structure is referred as
# Unordered Collections of Unique Elements and does not
# support operations like indexing or slicing
#
# from documentation:
# Like other collections, sets support x in set,
# len(set), and for x in set. Being an unordered collection,
# sets do not record element position or order of insertion.
# Accordingly, sets do not support indexing, slicing, or
# other sequence-like behavior.






