# course: Object-oriented programming, year 2, semester 1
# academic year: 2021-20
# author: B. Schoen-Phelan
# date: 11-11-2021
# purpose: Lab wk8 - Word Games

"""
    The game runs from here.
    All the functions are called from here.
    Both classes have their own object which are used to call the function.
    Both games modules are imported into here.
"""
from worddupe import WordDuplication
from wordscramb import WordScramble

# don't need to use WordGames class, because of inheritance

scrambled_words = WordScramble()
scrambled_words.word_play()

duplicated_word = WordDuplication()
duplicated_word.word_play()


