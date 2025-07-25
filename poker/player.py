class Player:
    def __init__(self, name, position, stack):
        self.name = name
        self.position = position
        self.stack = stack
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)