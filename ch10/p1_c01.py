'''
除了映射到二元组函数和只提供一个参数来实例化的方案外，我们还可以创建partial()函数。
这个函数可以用来实现可选参数。
通过调用partial()函数然后赋值给part_class,完成了与rank对象的关联。
可以使用同样的方式suit对象。
'''
from functools import partial
from Card import AceCard, FaceCard, NumberCard
from Suit import Club, Diamond, Heart, Spade
import random

def card7(rank, suit):
    part_class = {
        1: partial(AceCard, 'A'),
        11: partial(FaceCard, 'J'),
        12: partial(FaceCard, 'Q'),
        13: partial(FaceCard, 'K'),
    }.get(rank, partial(NumberCard, str(rank)))
    return part_class(suit)

class CardFactory:
    def rank(self, rank):
        self.class_, self.rank_str = {
            1: (AceCard, 'A'),
            11: (FaceCard, 'J'),
            12: (FaceCard, 'Q'),
            13: (FaceCard, 'K'),
        }.get(rank, (NumberCard, str(rank)))

    def suit(self, suit):
        return self.class_(self.rank_str, suit)

class Deck3(list):
    def __init__(self, decks=1):
        super().__init__()
        for i in range(decks):
            self.extend( card7(r+1, s) for r in range(13) for s in (Club, Diamond, Heart, Spade))
        random.shuffle(self)
        burn = random.randint(1,52)
        for i in range(burn): self.pop()

class Hand:
    def __init__(self, dealer_card):
        self.dealer_card = dealer_card
        self.cards = []
    def hard_total(self):
        return sum(c.hard for c in self.cards)
    def soft_total(self):
        return sum(c.soft for c in self.cards)

