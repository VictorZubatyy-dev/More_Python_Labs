# OOP 2021-22
# B. Schoen-Phelan
# October 2021
# Card Game a solution

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from random import shuffle

class CardGame(App):
    # The build method is the start point of the GUI application
    def build(self):
        # load card path strings in a list
        self.the_cards = self.load_cards()

        # build window. This is the same layout as in the example.
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.9)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}

        #add widgets to window

        # what this card_link contains depends on what was loaded
        # in the load_cards
        card_link = "cards/"+self.the_cards[0]+".jpeg"

        # we use the counter in a few places to check that we are
        # still within the bounds of our 10 cards. You could also
        # check if next of the list is valid, which is another way
        # of making sure that you don't run outside of your list.
        self.count_cards = 0

        self.current_card = Image(
            source=card_link,
            size_hint = (1,1),
            allow_stretch = True)
        self.window.add_widget(self.current_card)

        self.message_label = Label(
            text = "Guess if the next card will be higher or lower!"
        )
        self.window.add_widget(self.message_label)

        self.button_lower = Button(
                      text="Lower",
                      size_hint = (0.5, 0.3))
        self.button_lower.bind(on_press=self.lower)
        self.window.add_widget(self.button_lower)

        self.button_higher = Button(
                      text="Higher",
                      size_hint = (0.5, 0.3))
        self.button_higher.bind(on_press=self.higher)
        self.window.add_widget(self.button_higher)

        self.button_next = Button(
                      text="Next",
                      size_hint = (0.5, 0.3))
        self.button_next.bind(on_press=self.next_card)
        self.window.add_widget(self.button_next)

        return self.window

    def next_card(self, event):
        # we increase the counter by one each time we click on the next
        # button. That helps us to know if the next card is a valid
        # item or if we are outside of our bounds of 10. Another
        # solution would be to check if the next value of the list is
        # valid
        self.count_cards += 1

        # see comments above for why we check that we are checking that
        # this value is below 10.
        # The list has items from index 0 to index 9.
        if self.count_cards < 10:
            # building the path to the card
            card_link = "cards/"+self.the_cards[self.count_cards]+".jpeg"

            # updating the path of the Image widget, this was also
            # seen in the example GUI file.
            self.current_card.source = card_link


    def lower(self, event):
        # only check a card if we haven't yet gone through the 10.
        # an alternative check would be to see if the next index
        # position in the list is valid. The list holds values
        # from index 0 to index 9. Here we are checking for lower
        # than 9 because we need to know if there's a next card to
        # fetch its value.
        if self.count_cards < 9:

            # the pattern is similar to cards/10_clubs.jpeg
            # we get the index positions of the / and the _ and the
            # value of the card lies between them.
            start_pos_idx = self.current_card.source.find("/") + 1
            end_pos_idx = self.current_card.source.find("_")
            current_card_value = self.current_card.source[start_pos_idx:end_pos_idx]

            # the value could also come back as jack, king or queen, which are
            # not digits. In that case we set the value to 10.
            if not current_card_value.isdigit():
                current_card_value = 10

            # we do the same thing to retrieve the value of the card following the
            # curren one.
            start_pos_idx = self.the_cards[self.count_cards + 1].find("/")+1
            end_pos_idx = self.the_cards[self.count_cards + 1].find("_")
            next_card_value = self.the_cards[self.count_cards + 1][start_pos_idx:end_pos_idx]

            # this checks for king, queen and jack
            if not next_card_value.isdigit():
                next_card_value = 10

            # here we do the actual comparison checking
            if int(next_card_value) < int(current_card_value):
                self.message_label.text = "You won!"
            elif int(next_card_value) > int(current_card_value):
                self.message_label.text = "You lost"
            else: # we display this in case the next card has the same value as the current card
                self.message_label.text = "Nobody won, the next card is worth the same!"
        else:
            # no next value present, we are at the end of our list.
            self.message_label.text = "No more cards. The game is finished."

    def higher(self, event):
        # the higher callback function works very much the same as the lower
        # callback function. The difference is in the comparison of the values,
        # which are flipped around.
        # Alternatively, you could use the same callback for both buttons and
        # then check which button was checked and amend your if statement
        # accordingly.

        if self.count_cards < 9:
            # in theory we know the next part anyway, because it is always the same
            # but it is nice to remind ourselves how to find the positional index
            # of a character
            start_pos_idx = self.current_card.source.find("/") + 1
            end_pos_idx = self.current_card.source.find("_")
            current_card_value = self.current_card.source[start_pos_idx:end_pos_idx]

            if not current_card_value.isdigit():
                current_card_value = 10

            start_pos_idx = self.the_cards[self.count_cards + 1].find("/") + 1
            end_pos_idx = self.the_cards[self.count_cards + 1].find("_")
            next_card_value = self.the_cards[self.count_cards + 1][start_pos_idx:end_pos_idx]

            # this checks for king, queen and jack
            if not next_card_value.isdigit():
                next_card_value = 10

            if int(next_card_value) > int(current_card_value):
                self.message_label.text = "You won!"
            elif int(next_card_value) < int(current_card_value):
                self.message_label.text = "You lost!"
            else:
                self.message_label.text = "Nobody won, the next card is worth the same!"
        else:
            self.message_label.text = "No more cards. The game is finished."

    def load_cards(self):
        suits = ("hearts", "diamonds", "spades", "clubs")
        people = ("queen", "jack", "king")

        # a more elegant solution would be to use a queue
        # or a stack instead of a list.
        card_list = []

        for i in range(1, 11):
            for suit in suits:
                # cards.put(str(i)+"_"+suit)
                card_list.append(str(i) + "_" + suit)

        for suit in suits:
            for person in people:
                # cards.put(person+"_"+suit)
                card_list.append(person + "_" + suit)

        shuffle(card_list)

        return card_list[:10]


if __name__ == "__main__":
    CardGame().run()


