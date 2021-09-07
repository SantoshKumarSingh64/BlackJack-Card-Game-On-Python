class Card():

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return self.rank+" of "+self.suit

class Deck():

    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+='\n'+card.__str__()
        return "The Deck has : "+deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card=self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):

        while self.value>21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self,total=100):

        self.total=total
        self.bet = 0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet
