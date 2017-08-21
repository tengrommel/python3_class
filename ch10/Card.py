# coding:utf-8


class Card:
    insure = False

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()

    # 判断相等
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank and self.hard == other.hard and self.soft == other.soft

    def __repr__(self):
        return "{__class__.__name__}(suit={suit!r}, rank={rank!r})".format(__class__=self.__class__, **self.__dict__)

    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)


class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):
    insure = True

    def _points(self):
        return 1, 11


class FaceCard(Card):
    def _points(self):
        return 10, 10
