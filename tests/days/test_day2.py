from unittest import TestCase
import pytest
from days.day2 import calculate_score, game, match_winner, Winner, run


class TestDay1(TestCase):
    def setUp(self):
        self.data = ["A Y", "B X", "C Z"]

    def test_game(self):
        results = game(self.data)
        self.assertEqual(results["computer"], 15)
        self.assertEqual(results["player"], 15)

    def test_calculate_score(self):
        self.assertEqual(calculate_score("rock", Winner.DRAW), 4)
        self.assertEqual(calculate_score("rock", Winner.LOSE), 1)
        self.assertEqual(calculate_score("rock", Winner.WIN), 7)
        self.assertEqual(calculate_score("paper", Winner.DRAW), 5)
        self.assertEqual(calculate_score("paper", Winner.LOSE), 2)
        self.assertEqual(calculate_score("paper", Winner.WIN), 8)
        self.assertEqual(calculate_score("scissors", Winner.DRAW), 6)
        self.assertEqual(calculate_score("scissors", Winner.LOSE), 3)
        self.assertEqual(calculate_score("scissors", Winner.WIN), 9)

    def test_run_part_a(self):
        results = run('a', self.data)
        self.assertDictEqual(results, {"computer": 15, "player": 15})

    def test_run_part_b(self):
        results = run('b', self.data)
        self.assertDictEqual(results, {"computer": 15, "player": 12})


@pytest.mark.parametrize(
    "player_one,player_two,expected",
    [
        ("rock", "rock", Winner.DRAW),
        ("rock", "rock", Winner.DRAW),
        ("rock", "scissors", Winner.WIN),
        ("rock", "scissors", Winner.WIN),
        ("rock", "paper", Winner.LOSE),
        ("rock", "paper", Winner.LOSE),
        ("paper", "paper", Winner.DRAW),
        ("paper", "paper", Winner.DRAW),
        ("paper", "rock", Winner.WIN),
        ("paper", "rock", Winner.WIN),
        ("paper", "scissors", Winner.LOSE),
        ("paper", "scissors", Winner.LOSE),
        ("scissors", "scissors", Winner.DRAW),
        ("scissors", "scissors", Winner.DRAW),
        ("scissors", "paper", Winner.WIN),
        ("scissors", "paper", Winner.WIN),
        ("scissors", "rock", Winner.LOSE),
        ("scissors", "rock", Winner.LOSE)
    ]
)
def test_match_winner(player_one, player_two, expected):
    results = match_winner(player_one, player_two)
    assert results == expected
