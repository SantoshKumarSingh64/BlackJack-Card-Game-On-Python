def take_bet(chips):

    while True:

        try:
            chips.bet=int(input("How many chips would you like to bet : "))
        except:
            print("Sorry !!! You must enter an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry !!! You don't have enough chips. You have only ",chips.total)
            else:
                break

def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()

def hit_or_stand(deck,hand):

    global playing

    while True:

        x = input("Hit or Stand ? Enter h or s : ")

        if x[0].lower() == 'h':
            hit(deck,hand)
            show_hit_card(hand)
        elif x[0].lower() == 's':
            print("Player stands ,Now dealer's turn")
            break
        else:
            print("Sorry !!! I didn't understand that please enter h or s only!")
            continue


def show_hit_card(player):
    print('\n')
    print("Now ,After hit player's Hand :")
    print(" --------------------")
    for card in player.cards:
        print("|"+(str(card)).center(20)+"|")
    print(" --------------------") 


def show_some(player,dealer):

    print('\n')
    print("Dealer's Hand :")
    print(" --------------------")
    print("|"+"One Card Hidden".center(20)+"|")
    print("|"+(str(dealer.cards[1])).center(20)+"|")
    print(" --------------------")
    print('\n')
    print("Player's Hand :")
    print(" --------------------")
    for card in player.cards:
        print("|"+(str(card)).center(20)+"|")
    print(" --------------------")

def show_all(player,dealer):

    print('\n')
    print("Dealer's Hand :")
    print(" --------------------")
    for card in dealer.cards:
        print("|"+(str(card)).center(20)+"|")
    print(" --------------------")    
    print('\n')
    print("Player's Hand :")
    print(" --------------------")
    for card in player.cards:
        print("|"+(str(card)).center(20)+"|")
    print(" --------------------")

def player_busts(player,dealer,chips):
    print("Player Busted !!! Dealer Won")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player Won !!!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busted,Player Won !!!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer Won !!!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and player tie !!! PUSH")
