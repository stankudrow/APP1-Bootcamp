from collections import Counter

from players import Player
from states import Moves


class GameError(Exception):
    pass


class Game:
    def __init__(self, *, matches: int = 10):
        self._matches = matches
        self._rating = Counter()

    def play(self, player1: Player, player2: Player) -> None:
        p1_prev_move: None | Moves = None
        p2_prev_move: None | Moves = None
        for round_ in range(1, self._matches + 1):
            p1_move = player1.move(p2_prev_move, round_)
            p2_move = player2.move(p1_prev_move, round_)
            match_ = (
                f"match #{round_}: "
                f"player1_move = {p1_move} vs player2_move = {p2_move}"
            )
            print(match_)
            if (p1_move, p2_move) == (Moves.cheat, Moves.cheat):
                self._rating[str(player1)] += 0
                self._rating[str(player2)] += 0
            if (p1_move, p2_move) == (Moves.cooperate, Moves.cooperate):
                self._rating[str(player1)] += 2
                self._rating[str(player2)] += 2
            if (p1_move, p2_move) == (Moves.cheat, Moves.cooperate):
                self._rating[str(player1)] += 3
                self._rating[str(player2)] -= 1
            if (p1_move, p2_move) == (Moves.cooperate, Moves.cheat):
                self._rating[str(player1)] -= 1
                self._rating[str(player2)] += 3
            player1.update(p2_move, round=round_)
            player2.update(p1_move, round=round_)
            p1_prev_move = p1_move
            p2_prev_move = p2_move
        player1.reset()
        player2.reset()

    def top3(self) -> None:
        rating = ""
        for rank, (player, score) in enumerate(self._rating.most_common(3), start=1):
            rating += f"{rank}: {player} ({score})\n"
        print(rating.rstrip())
