import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame()

    def test_check_for_ace(self):
        card = Card("spade",1)
        actual = self.card_game.check_for_ace(card)
        self.assertEqual(True,actual)

    def test_highest_card(self):
        card1 = Card("diamond",5)
        card2 = Card("club",10)
        actual = self.card_game.highest_card(card1,card2)
        self.assertEqual(card2,actual)

    def test_cards_total(self):
        card1 = Card("diamond",5)
        card2 = Card("club",10)
        card3 = Card("diamond",2)
        cards = [card1,card2,card3]
        actual = self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 17",actual)