import random


class Card:
    """The basic representation of a card"""

    values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    suits = [("Hearts", "R"), ("Diamonds", "R"), ("Spades", "B"), ("Clubs", "B")]

    def __init__(self, value, suit, color):
        self.value = value
        self.suit = suit
        self.color = color

        self.name = str(value) + suit[0]

    def __repr__(self):
        return self.name


class Pile:
    """Multiple cards in a set"""

    def __init__(self, *args):
        self.cards = list(args)

    def __repr__(self):
        return str(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def unshuffle(self):
        self.cards.sort(key=lambda card: card.name[:0])

    def add(self, card):
        """Adds a card object 'card'"""
        self.cards.append(card)

    def take(self, card):
        """Removes all card objects with name 'card'"""
        outlaws = []
        
        for c in self.cards:
            if c.name == card:
                outlaws.append(c)

        for c in outlaws:
            self.cards.remove(c)


class Deck(Pile):
    """52 card Pile, 13 of each suit"""

    start = [Card(value, suit, color)
             for value in Card.values
             for suit, color in Card.suits]
    
    def __init__(self):
        Pile.__init__(self, *Deck.start)
        self.unshuffle()

if __name__ == "__main__":
    # debug stuff
    
    d = Deck()
    print(d)
