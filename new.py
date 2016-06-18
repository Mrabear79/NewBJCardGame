from random import choice as rc


def total(hand):
    values = []
    for v in hand:
        values.append(v.value)
    aces = values.count(11)
    t = sum(values)
    if t > 21 and aces > 0:
        while aces > 0 and t > 21:
            t -= 10
        aces -= 1
    return t


class Card():

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck():

    def __init__(self):
        self.deck = []

    def create_deck(self):
        suit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        for su in suit:
            x = 0
            for rk in rank:
                self.deck.append(Card(su, rk, cards[x]))
                x += 1
compwin = 0
playwin = 0
deck = Deck()
deck.create_deck()
print(deck.deck)
while True:
    player = []
    player.append(rc(deck.deck))
    player.append(rc(deck.deck))
    playbust = False
    compbust = False
    while True:
        tp = total(player)
        print("The players cards are %s with a total of %d" % (player, tp))
        if tp > 21:
            print("Player busted!")
            playbust = True
            if compbust >= False:
                print("Computer wins!!")
                compwin += 1
            break
        elif tp == 21:
            print("\a BLACKJACK!!!")
            playwin += 1
            break
        else:
            hs = input("Hit or Stand (h or s): ").lower()
            if 'h' in hs:
                player.append(rc(deck.deck))
            else:
                break
    while True:
        comp = []
        comp.append(rc(deck.deck))
        comp.append(rc(deck.deck))
        while True:
            tc = total(comp)
            if tc < 17:
                comp.append(rc(deck.deck))
            else:
                tc > 17
                break
        print("The computer has %s with a total of %d" % (comp, tc))
        if tc > 21:
            print("Computer busted!")
            compbust = True
            if playbust = True:
                print("Player wins!")
                playwin += 1
            break
        elif tc == 21:
            print("\a BLACKJACK!!!")
            compwin += 1
            break
        elif tc > tp:
            print("Computer wins!")
            compwin += 1
        elif tc == tp:
            print("Draw!")
        elif tp > tc:
                print("Player wins!")
                playwin += 1
        elif compbust = True:
                print("Computer wins!")
                compwin += 1
        break
    print
    print("Player Wins = %d  Computer Wins = %d" % (playwin, compwin))
    exit = input("Press Enter for next game or (q to quit): ").lower()
    if 'q' in exit:
        break
    print
print
print("Thanks for playing blackjack!")
