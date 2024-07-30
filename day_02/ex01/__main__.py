from itertools import combinations
from random import shuffle

from game import Game
from players import (
    Cheater,
    Cooperator,
    Copycat,
    Detective,
    Grudger,
    MyPlayer,
)


if __name__ == "__main__":
    num_of_matches = 10
    game = Game(matches=num_of_matches)

    players = [
        Cheater(),
        Cooperator(),
        Copycat(),
        Detective(),
        Grudger(),
        # MyPlayer(matches=num_of_matches),
    ]
    shuffle(players)

    pairs = combinations(players, 2)
    for player1, player2 in pairs:
        print(f"pair = {(player1, player2)}")
        game.play(player1, player2)
        game.top3()
