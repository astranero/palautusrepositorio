import unittest
from statistics import Statistics
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_correct_player(self):
        self.assertEqual(self.statistics.search("Semenko").name, "Semenko")

    def test_search_returns_none_if_player_not_found(self):
        self.assertEqual(self.statistics.search("Noname"), None)

    def test_team_returns_correct_team_players(self):
        players = self.statistics.team("PIT")
        for player in players:
            self.assertEqual(player.team, "PIT")
   
    def test_top_returns_correct_val(self):
        top_player = self.statistics.top(1)
        self.assertEqual(top_player[0].name, "Gretzky")
    
    def test_top_returns_correct_sortby_points(self):
        top_player = self.statistics.top(1,SortBy.POINTS)
        self.assertEqual(top_player[0].name, "Gretzky")
   
    def test_top_returns_correct_sortby_goals(self):
        top_player = self.statistics.top(1, SortBy.GOALS)
        self.assertEqual(top_player[0].name, "Lemieux")

    def test_top_returns_correct_sortby_assists(self):
        top_player = self.statistics.top(1,SortBy.ASSISTS)
        self.assertEqual(top_player[0].name, "Gretzky")
   

   # ...
