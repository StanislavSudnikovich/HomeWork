class CardDesc:

    def __init__(self, suit='Spades', value='2'):
        self.suit = suit
        self.value = value
        self.all_suit = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        self.all_value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']

    def __iter__(self):
        return self

    def __next__(self):
        if self.suit in self.all_suit and self.value == 'a' and self.suit != 'Clubs':
            self.suit = self.all_suit[self.all_suit.index(self.suit) + 1]
            self.value = self.all_value[0]
            return self.value + ' ' + self.suit
        elif self.suit in self.all_suit and self.value in self.all_value and self.value != 'a':
            self.value = self.all_value[self.all_value.index(self.value) + 1]
            return self.value + ' ' + self.suit
        else:
            raise StopIteration


card = CardDesc()

print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
print(next(card))
