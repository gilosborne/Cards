print("Hello World")

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):

# class Player(object):
#     def __init__(self):


card = Card("Clubs", 6)
card.show()