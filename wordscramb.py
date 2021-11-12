from WordGames import WordGames


class WordScramble(WordGames):#you implement this and provide docstrings
    """
        Class to represent the word game's child class.
        ...
        Attributes:
        -----------
            sentence : str
            Stores the input from user after it has been put into a list.

            scrambled_list : list
            Store the scrambled word or sentence.

            scrambled_sentence : str
            Stores the scrambled word or sentence from the scrambled_list list in a string.

        Methods:
        --------
            word_play:
                Contains logic for scrambling the word or sentence.
        """
    def word_play(self):
        """
            This function implements the game logic for scrambling a word or a sentence.
            It overrides the parent class function.

            Parameters: None.
            -----------

            Returns: None.
            --------
        """
        sentence = self.the_words.strip().split()
        scrambled_list = []
        scrambled_sentence = scrambled_list

        for word in sentence:
            char_list = list(word)
            first_letter = word[0:1]
            last_letter = word[-1]
            char_list[0] = last_letter
            char_list[-1] = first_letter
            scrambled_word = "".join(char_list)
            scrambled_list.append(scrambled_word)
            scrambled_sentence = " ".join(scrambled_list)
        print(scrambled_sentence)


