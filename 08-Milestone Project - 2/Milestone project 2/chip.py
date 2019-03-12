
class Chip():
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet * 2
        self.bet = 0

    def draw(self):
        self.total += self.bet
        self.bet = 0
    
    def lose_bet(self):
        
        self.bet = 0

    def take_bet(self):
        while True:
            try:
                print(f'current balance is {self.total}.')
                wage = int(input('How much are you betting? '))
                if wage > self.total:
                    print('You do not have enough chips.')
                else:
                    self.total -= wage
                    self.bet = wage
                    break
            except:
                print('Please input a valid wage.')
                continue
                
