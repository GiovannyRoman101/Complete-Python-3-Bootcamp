import random
import card

suits = ('Hearts', 'Diamonds', 'Spade', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(card.Card(suit,rank))

    def __str__(self):
        cards = ''
        for card in self.deck:
            cards += str(card) +'\n'
        return cards

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

