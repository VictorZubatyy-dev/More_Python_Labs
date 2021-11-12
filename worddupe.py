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
    def word_play(self):
        """
            This function implements the game logic for duplicating a word or a sentence.
            It overrides the parent class function.

            Parameters: None.
            -----------

            Returns: None.
            --------
            """
        duplicated_sentence = self.the_words
        print(duplicated_sentence * 2)
