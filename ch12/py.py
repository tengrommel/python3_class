class Hand:
    def __str__( self ):
        return ", ".join( map(str, self.card) )
    def __repr__( self ):
        return "{__class__.__name__}({dealer_card!r}, {_cards_str})".format(
        __class__=self.__class__,
        _cards_str=", ".join( map(repr, self.card) ),
        **self.__dict__ )
    def split( self, deck ):
        """Updates this hand and also returns the new hand."""
        assert self._cards[0].rank == self._cards[1].rank
        c1= self._cards[-1]
        del self.card
        self.card= deck.pop()
        h_new= self.__class__( self.dealer_card, c1, deck.pop() )
        return h_new

class Hand_Lazy(Hand):
    def __init__( self, dealer_card, *cards ):
        self.dealer_card= dealer_card
        self._cards= list(cards)
    @property
    def total( self ):
        delta_soft = max(c.soft-c.hard for c in self._cards)
        hard_total = sum(c.hard for c in self._cards)
        if hard_total+delta_soft <= 21: return hard_total+delta_soft
        return hard_total
    @property
    def card( self ):
        return self._cards
    @card.setter
    def card( self, aCard ):
        self._cards.append( aCard )
    @card.deleter
    def card( self ):
        self._cards.pop(-1)

class Hand_Eager(Hand):
    def __init__(self, dealer_card, *cards):
        self.dealer_card=dealer_card
        self.total = 0
        self._delta_soft = 0
        self._hard_total = 0
        self._cards = list()
        for c in cards:
            self.card = c

    @property
    def card(self):
        return self._cards

    @card.setter
    def card(self, aCard):
        self._cards.append(aCard)
        self._delta_soft = max(aCard.soft - aCard.hard, self._delta_soft)
        self._hard_total += aCard.hard
        self._set_total()

    @card.deleter
    def card(self):
        removed = self._cards.pop(-1)
        self._hard_total -= removed.hard
        # Issue: was this the only ace?
        self._delta_soft = max(c.soft - c.hard for c in self._cards)
        self._set_total()

    def _set_total(self):
        if self._hard_total + self._delta_soft <= 21:
            self.total = self._hard_total + self._delta_soft
        else:
            self.total = self._hard_total