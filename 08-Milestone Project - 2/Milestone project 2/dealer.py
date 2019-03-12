import hand
import deck

class Dealer():

    def __init__(self):
        self.deck = deck.Deck()
        self.hand = hand.Hand()

    def deal(self, dealing_to):
        card = self.deck.deal()
        dealing_to.hand.add_card(card)
