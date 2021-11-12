from WordGames import WordGames


class WordDuplication(WordGames):# you implement this and provide docstrings
    """
            Class to represent the word game's child class.
            ...
            Attributes:
            -----------
                sentence : str
                Stores the input from user.

                duplicated_sentence : str
                Stores the duplicated sentence.

            Methods:
            --------
                word_play:
                    Contains logic for duplicating a word or sentence.

                the_words:
                    Return the duplicated sentence.
            """
    def __init__(self):
        """
                Constructs the necessary attributes for the
                WordDuplication object.

                Parameters: None.
                -----------

                Instance variables:
                -------------------
                    sentence : str
                    Stores the input from user.

                    duplicated_sentence : str
                    Stores the duplicated sentence.
                """
        super().__init__()
        self.sentence = self._my_words
        self.duplicated_sentence = self.sentence

    def word_play(self):
        """
            This function implements the game logic for duplicating a word or a sentence.
            It overrides the parent class function.

            Parameters: None.
            -----------

            Returns: None.
            --------
            """
        self.duplicated_sentence = self.sentence

    @property
    def the_words(self):
        """
            This function returns the duplicated sentence. It overrides the parent class function.
            It uses the instance variable duplicated_sentence and sentence to
            then return a duplicated sentence.

            Parameters: None.
            -----------

             Returns:
                 sentence : str
                 The value of the word or sentence that has
                 been inputted by a user.

                 duplicated_sentence : str
                 The duplicated sentence which is essentially sentence.
            --------
            """
        return 'Duplicated input: ' + self.sentence + " " + self.duplicated_sentence
