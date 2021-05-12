from abc import ABC, abstractmethod
class Clothing(ABC):
    def __init__(self, vh):
        self.vh = vh
    @abstractmethod
    def fabr_consump(self):
        pass

class Coat(Clothing):
    def __init__(self, v):
        super().__init__(v)
        self.v = v
    @property
    def fabr_consump(self):
        return round(self.v/6.5 + 0.5, 2)

    @property
    def result_consump(self):
        return (f'Расход ткани на пошив пальто {self.v} размера: {self.v/6.5 + 0.5 :.2f} кв.м.')

class Suit(Clothing):
    def __init__(self, h):
        super().__init__(h)
        self.h = h

    @property
    def fabr_consump(self):
        return round(2*self.h + 0.3, 2)

    @property
    def result_consump(self):
        return (f'Расход ткани на пошив костюма на рост {self.h} м: {2*self.h + 0.3 :.2f} кв.м.')

mycoat = Coat(46)
print(mycoat.result_consump)
mysuit = Suit(1.66)
print(mysuit.result_consump)
print(f"Общий расход ткани: {mycoat.fabr_consump + mysuit.fabr_consump} кв.м.")