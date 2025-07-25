from poker.deck import Deck
from poker.player import Player

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    player = Player("John", "BB", 500)
    player.hand = deck.deal(2)
    print(player.hand)