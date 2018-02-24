class Card:
    insure = False
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()

class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)

'''
__str__方法
1.调用map函数对集合中的每个对象使用str()方法，这会基于返回的字符串集合创建一个迭代器。
2.用"，".join()将所有对象的字符串标识连接成一个长字符串。
__repr__方法
1.调用map函数对集合中的每个对象应用repr()方法，这会基于返回的结果集创建一个迭代器。
2.使用".".join()连接所有对象的字符串表示。
3.用__class__、集合字符串和__dict__中的不同属性创建一些关键字。
'''
class Hand:
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)
    def __str__(self):
        return ", ".join(map(str, self.cards))
    def __repr__(self):
        return "{__class__.__name__}({dealer_card!r},{_cards_str})".format(
            __class__=self.__class__,
            _cards_str = ", ".join(map(repr, self.cards)),
            **self.__dict__)

class Card2:
    insure = False
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft
    def __repr__(self):
        return "{__class__.__name__}(suit={suit!r}, rank={rank!r})".format(___class__=self.__class__, **self.__dict__)
    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == self.rank
    def __hash__(self):
        return hash(self.suit)^hash(self.rank)
