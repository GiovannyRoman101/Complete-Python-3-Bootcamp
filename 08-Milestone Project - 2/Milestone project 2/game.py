import deck
import chip
import player
import dealer

def show_some(player,dealer):
    playerhand = []
    print('\n')
    print(f"Player's score: {player.hand.value}")
    print("Player's hand:")

    for card in player.hand.cards:
        playerhand.append(str(card))
    pstr = ', '.join(playerhand)
    print(pstr[::1]+'\n')

    print("Dealer's Hand:")
    print(f'{dealer.hand.cards[0]}')
    

def show_all(player, dealer):
    playerhand = []
    dealerhand = []
    print('\n')
    print(f"Player's score: {player.hand.value}")
    print("Player's hand:")

    for card in player.hand.cards:
        playerhand.append(str(card))

    pstr = ', '.join(playerhand)
    print(pstr[::1]+'\n')
    
    for card in dealer.hand.cards:
        dealerhand.append(str(card))

    dstr = ', '.join(dealerhand)
    print(f"Dealer's score: {dealer.hand.value}")
    print("Dealer's Hand:")
    print(dstr[::1])
    

def replay():
    
    while True:
        user_response = input('Do you want to play again? ')
        if(user_response.upper() == 'Y' or user_response.upper() == 'YES'):
            return True
        elif user_response.upper() == 'N' or user_response.upper() == 'NO':
            return False
        else:
            print("Please enter yes or no.")



def start_game():
    print('Welcome to Black Jack')
    player_human = player.Player()
    game_dealer = dealer.Dealer()
    playing = True

    while playing:
        print(f'current balance: {player_human.chips.total} ')
        if player_human.chips.total <= 0:
            print("You ran out of chips")
            break

        game_dealer.deck.shuffle()
        player_human.chips.take_bet()

        ##deal two cards to player and dealer
        game_dealer.deal(player_human)
        game_dealer.deal(game_dealer)
        game_dealer.deal(player_human)
        game_dealer.deal(game_dealer)

        ## ask user if want to hit or stand
        while player_human.hand.value < 21 :
            show_some(player_human,game_dealer)
            if(player_human.hit_or_stand()):
                game_dealer.deal(player_human)
            else:
                break
        
        
        if player_human.hand.value == 21 :
            player_human.chips.win_bet()
            show_some(player_human,game_dealer)
            print("Player wins")
            
        elif player_human.hand.value > 21 :
            player_human.chips.lose_bet()
            show_some(player_human,game_dealer)
            print('Player Bust')
            
        else:
            ## need to fix
            show_all(player_human,game_dealer)
            while game_dealer.hand.value < player_human.hand.value :
                game_dealer.deal(game_dealer)
                show_all(player_human,game_dealer)
            if game_dealer.hand.value > player_human.hand.value and game_dealer.hand.value <=21:
                player_human.chips.lose_bet()
                print("Player bust")
            elif game_dealer.hand.value > 21:
                print("Player wins")
                player_human.chips.win_bet()
            elif game_dealer.hand.value == player_human.hand.value:
                print("draw")
                player_human.chips.draw()

        ## need to reset cards
        if(player_human.chips.total > 0):
            game_dealer = dealer.Dealer()
            player_human.reset_hand()
            if not replay() :
                break
    print('END GAME')
        
        


if __name__ == "__main__":

    start_game()