class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type
    def show(self):
        print("Value: ", self.value, "Type: ", self.type)
class Deck:
    def __init__(self, name):
        self.deck = []
        self.name = name
        for i in ["clubs", "diamonds", "hearts", "spades"]:
            for j in range(1,14):
                self.deck.append( Card(j, i ) )
    def show(self):
        print("\n", "*"*30, self.name, "*"*30)
        for card in self.deck:
            card.show()
d1 = Deck("First Deck")
d1.show()
d2 = Deck("Second Deck")
d2.show()


def varargs(arg1, *args):
    print("Got "+arg1+" and "+ ", ".join(args))
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three") # output: "Got one and two, three"
