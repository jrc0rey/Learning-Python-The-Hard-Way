#Create a deck of cards with classes

class Card(object):
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def show(self):
        print('%s of %s' % (self.value, self.suit ))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for v in range(1,14):
                self.cards.append(Card(s,v))
                # print('%s of %s' % (v,s ))
    def show(self):
        for c in self.cards:
            c.show()

class Player(object):
    pass

# card = Card('hearts', 10)
# card.show()

Deck()
