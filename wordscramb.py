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

            the_words:
                Return the scrambled sentence.
        """
    def __init__(self):
        """
        Constructs the necessary attributes for the
        WordScramble object.

        Parameters: None.
        -----------

        Instance variables:
        -------------------
            sentence : str
            Stores the input from user after it has been put into a list.

            scrambled_list : list
            Store the scrambled word or sentence.

            scrambled_sentence : str
            Stores the scrambled word or sentence from the scrambled_list list in a string.
        """

        super().__init__()
        self.sentence = self._my_words.strip().split()
        self.scrambled_list = []
        self.scrambled_sentence = self.scrambled_list

    def word_play(self):
        """
            This function implements the game logic for scrambling a word or a sentence.
            It overrides the parent class function.

            Parameters: None.
            -----------

            Returns: None.
            --------
        """
        for word in self.sentence:
            char_list = list(word)
            first_letter = word[0:1]
            last_letter = word[-1]
            char_list[0] = last_letter
            char_list[-1] = first_letter
            scrambled_word = "".join(char_list)
            self.scrambled_list.append(scrambled_word)
            self.scrambled_sentence = " ".join(self.scrambled_list)

    @property
    def the_words(self):
        """
            This function returns the scrambled sentence. It overrides the parent class function.

            Parameters: None.
            -----------

             Returns:
                 scrambled_sentence : str
                 The scrambled sentence.
            --------
                            """
        print("scrambled sentence:")
        return self.scrambled_sentence


