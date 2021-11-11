from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from random import shuffle
import os

class CardGame(App):
    # currentCard = 0
    # nextCard = 0
    def build(self):
        self.cards, self.card_values = self.load_cards()
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}


        self.current_card = Image(
            source = "cards/" + self.cards[0],
            size_hint = (1,1),
            allow_stretch = True)
        self.window.add_widget(self.current_card)

        #use this as a variable to access the next card path, not displayed
        self.next_cards = Image(
            source="cards/" + self.cards[1],
            size_hint=(0, 0),
            allow_stretch=True)
        self.window.add_widget(self.next_cards)

        self.next_button = Button(
            text="Next",
            size_hint=(1, 0.3),
            bold=True,
            background_color="#00FFCE"
        )
        self.window.add_widget(self.next_button)
        self.next_button.bind(on_press=self.next_card)

        self.higher_button = Button(
            text="Higher",
            size_hint=(1, 0.3),
            bold=True,
            background_color="#00FFCE"
        )
        self.window.add_widget(self.higher_button)
        self.higher_button.bind(on_press=self.check_higher)

        self.lower_button = Button(
            text="Lower",
            size_hint=(1, 0.3),
            bold=True,
            background_color="#00FFCE"
        )
        self.window.add_widget(self.lower_button)
        self.lower_button.bind(on_press=self.check_lower)

        self.label = Label(
            font_size=38,
            color="#00FFCE")
        self.window.add_widget(self.label)

        # self.you_won= Label(
        #     font_size=38,
        #     color="#00FFCE")
        # self.window.add_widget(self.you_won)
        #
        # self.you_lost = Label(
        #     font_size=38,
        #     color="#00FFCE")
        # self.window.add_widget(self.you_lost)

        # self.window.add_widget(self.higher_button)
        # self.higher_button.bind(on_press=self.check_higher)

        return self.window

    def load_cards(self):
        card_list = []
        card_values = {}
        #load the cards in from their directory and put into a list
        for card in os.listdir('cards'):
            card_list.append(card)
            if card[0].isdigit() and card[1] == "_":
                card_values[card] = card[0]
            elif card[0].isalpha():
                card_values[card] = 15
            else:
                card_values[card] = 10
        shuffle(card_list)
        return card_list[:10], card_values

    def next_card(self, event):
        for card in range(len(self.cards) - 1):
                current_card = self.cards[card]
                next_card = self.cards[card + 1]
                self.current_card.source = "cards/" + current_card
                self.next_cards.source = "cards/" + next_card
                self.cards.remove(current_card)

                if len(self.cards) == 1:
                    self.label.text = "You have ran out of cards"
                return
        # return self.check_higher(current_card, next_card)


    def check_higher(self, event):
        #remove the cards/ path infront so that we can access value of card
        current_card = self.current_card.source[6:]
        next_card = self.next_cards.source[6:]

        if int(self.card_values[next_card]) > int(self.card_values[current_card]):
            self.label.text = "You won"
        elif int(self.card_values[next_card]) < int(self.card_values[current_card]):
            self.label.text = "You lost"
        elif int(self.card_values[next_card]) == int(self.card_values[current_card]):
            self.label.text = "Both same"
        else:
            self.label.text = "You ran out of cards"

            print(next_card)
            print(current_card)

    def check_lower(self, event):
        current_card = self.current_card.source[6:]
        next_card = self.next_cards.source[6:]

        if int(self.card_values[next_card]) < int(self.card_values[current_card]):
            self.label.text = "You won"
        elif int(self.card_values[next_card]) > int(self.card_values[current_card]):
            self.label.text = "You lost"
        elif int(self.card_values[next_card]) == int(self.card_values[current_card]):
            self.label.text = "Both same"
        else:
            self.label.text = "You ran out of cards"

if __name__ == "__main__":
    CardGame().run()