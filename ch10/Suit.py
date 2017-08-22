# coding:utf-8
from Card import AceCard, NumberCard


class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return self.symbol

Club, Diamond, Heart, Spade = Suit('Club','♣'), Suit('Diamond','♦'), Suit('Heart','♥'), Suit('Spade','♠')

d2 = [ AceCard('A', Spade), NumberCard('2', Spade), NumberCard('3', Spade), ]