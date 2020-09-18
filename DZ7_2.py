from abc import ABC, abstractmethod


class Menswear(ABC):
    @property
    @abstractmethod
    def take(self):
       pass


class Coat(Menswear):
    def __init__(self, v):
        self.v = int(v)

    @property
    def take(self):
        return self.v/6.5 + 0.5


class Suit(Menswear):
    def __init__(self, h):
        self.h = h

    @property
    def take(self):
        return 2 * self.h + 0.3


my_coat = Coat(42)
my_suit = Suit(1.76)
print(my_coat.take, my_suit.take)



