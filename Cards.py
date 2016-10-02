class Card:

    suits = [("Hearts", "R"), ("Diamonds", "R"), ("Spades", "B"), ("Clubs", "B")]

    def __init__(self, value, suit, color):
        self.value = value
        self.suit = suit
        self.color = color

        self.name = suit[0] + str(value)

    def __repr__(self):
        return str(self.value) + " of " + str(self.suit)


class Pile:

    def __init__(self, *args):
        self.cards = set(args)

    def __repr__(self):
        return str(self.cards)

    def add(self, card):
        self.cards.append(card)

    def take(self, card):
        outlaws = []
        
        for c in self.cards:
            if c.name == card:
                outlaws.append(c)

        for c in outlaws:
            self.cards.remove(c)


class Deck(Pile):

    # LEFT OFF HERE AND I HATE IT
    default_ = "DONT KNOW"
    
    def __init__(self, [Card(value, suit, color) for ])

if __name__ == "__main__":
    c = Card(2, Card.suits[0][0], Card.suits[0][1])
    d = Card(3, Card.suits[1][0], Card.suits[1][1])
    
    p = Pile(c, d)
    p.take("D3")
    
    print(c)
    print(p)
