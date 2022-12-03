from typing import List
from enum import Enum


class Winner(Enum):
    DRAW: int = 0
    WIN: int = 1
    LOSE: int = 2


WINNING_MAP = {
    "rock": {"rock": Winner.DRAW, "paper": Winner.LOSE, "scissors": Winner.WIN},
    "paper": {"rock": Winner.WIN, "paper": Winner.DRAW, "scissors": Winner.LOSE},
    "scissors": {"rock": Winner.LOSE, "paper": Winner.WIN, "scissors": Winner.DRAW},
}

PLAY_MAP = {
    "a": "rock",
    "b": "paper",
    "c": "scissors",
    "x": "rock",
    "y": "paper",
    "z": "scissors",
}

BASE_POINTS = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}


def match_winner(player: str, computer: str) -> int:
    return WINNING_MAP[player][computer]


def calculate_score(hand, result):
    base_score = BASE_POINTS[hand]

    if result == Winner.LOSE:
        return base_score + 0
    elif result == Winner.DRAW:
        return base_score + 3
    else:
        return base_score + 6


def get_player_hand_based_on_predictive_strategy(computer, player) -> str:
    predictive_winning_map = {v: k for k, v in WINNING_MAP[computer].items()}
    prediction_inverse = {"x": Winner.WIN, "y": Winner.DRAW, "z": Winner.LOSE}
    return predictive_winning_map[prediction_inverse[player]]


def game(game_data: List[str], predictive_mode=False) -> dict:
    points = {"computer": 0, "player": 0}
    for game_round in game_data:

        # Get Computer and Player hands
        hand = [play.lower() for play in game_round.split(" ")]
        computer = PLAY_MAP[hand[0]]
        player = PLAY_MAP[hand[1]]

        if predictive_mode:
            player = get_player_hand_based_on_predictive_strategy(computer, hand[1])

        # Get Winner and Calculate Scores
        result = match_winner(player, computer)
        if result == Winner.DRAW:
            points["player"] += calculate_score(player, Winner.DRAW)
            points["computer"] += calculate_score(computer, Winner.DRAW)
        elif result == Winner.LOSE:
            points["player"] += calculate_score(player, Winner.LOSE)
            points["computer"] += calculate_score(computer, Winner.WIN)
        else:
            points["player"] += calculate_score(player, Winner.WIN)
            points["computer"] += calculate_score(computer, Winner.LOSE)

    return points


def run(part: str, data: List[str]):
    if part == "a":
        return game(data)

    if part == "b":
        return game(data, predictive_mode=True)
