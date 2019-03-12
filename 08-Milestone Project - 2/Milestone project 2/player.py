import hand
import chip


class Player():

    def __init__(self):
        self.hand = hand.Hand()
        self.chips = chip.Chip()

    def reset_hand(self):
        self.hand = hand.Hand()

    def hit_or_stand(self):
        while True:
            ans = input('Hit or Stand? ')
            if ans.upper() == 'HIT':
                return True
            elif ans.upper() == 'STAND':
                return False
            else:
                print('Please Enter hit or stand.')
