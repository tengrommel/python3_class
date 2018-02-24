from Card import AceCard, NumberCard, FaceCard
from Suit import Club, Diamond, Heart, Spade


def card(rank, suit):
    if rank == 1: return AceCard('A', suit)
    elif 2 <= rank < 11: return NumberCard(str(rank), suit)
    elif 11 <= rank < 14: name = {11: 'J', 12: 'Q', 13: 'K'}[rank]; return FaceCard(name, suit)
    raise Exception("Design Failure")

# This function builds a Card from a numeric rank and a Suit object.
if __name__ == '__main__':
    deck = [card(rank, suit) for rank in range(1, 14) for suit in (Club, Diamond, Heart, Spade)]
