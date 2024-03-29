#https://www.youtube.com/watch?v=t8YkjDH86Y4 at 11 minutes
import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))
            #print(s)

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


    def draw(self):
        return self.cards.pop()

# class Player(object):
#     def __init__(self):


#This is where the classes are run

deck = Deck()
deck.shuffle()

card = deck.draw()
card.show()