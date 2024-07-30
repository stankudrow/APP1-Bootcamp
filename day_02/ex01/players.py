import abc
from random import choice

from states import Moves


class Player(abc.ABC):
    def __init__(self, *, matches: None | int = None) -> None:
        self._matches = matches

    def __str__(self) -> str:
        return self.__class__.__name__

    @abc.abstractmethod
    def move(self, other: None | Moves = None, round: None | int = None) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def reset(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, other_move: Moves, round: None | int = None) -> None:
        raise NotImplementedError


class Cheater(Player):
    def move(self, other: None | Moves = None, round: None | int = None) -> str:
        return Moves.cheat

    def reset(self) -> None:
        return None

    def update(self, other_move: Moves, round: None | int = None) -> None:
        return None


class Cooperator(Player):
    def move(self, other: None | Moves = None, round: None | int = None) -> str:
        return Moves.cooperate

    def reset(self) -> None:
        return None

    def update(self, other_move: Moves, round: None | int = None) -> None:
        return None


class Copycat(Player):
    def move(self, other: None | Moves = None, round: None | int = None) -> str:
        if round == 1:
            return Moves.cooperate
        if not other:
            return choice([Moves.cheat, Moves.cooperate])
        if other == Moves.cooperate:
            return Moves.cooperate
        return Moves.cheat

    def reset(self) -> None:
        return None

    def update(self, other_move: Moves, round: None | int = None) -> None:
        return None


class Detective(Player):
    def __init__(self) -> None:
        self._is_cheated = False
        self._moves = [Moves.cooperate, Moves.cheat, Moves.cooperate, Moves.cooperate]

    def move(self, other: None | Moves = None, round: None | int = None) -> str:
        if round < 1:
            raise ValueError(f"round value {round} is less than 1")
        if round < 5:
            return self._moves[round - 1]
        if self._is_cheated:
            return Copycat().move(other=other, round=round)
        return Cheater().move(other=other, round=round)

    def reset(self) -> None:
        self._is_cheated = False

    def update(self, other_move: Moves, round: None | int = None) -> None:
        if other_move == Moves.cheat:
            self._is_cheated = True


class Grudger(Player):
    def __init__(self, *, matches: None | int = None) -> None:
        super().__init__(matches=matches)
        self._strategy = Cooperator()

    def move(self, other: None | Moves = None, round: None | int = None) -> str:
        return self._strategy.move(other=other, round=round)

    def reset(self) -> None:
        self._strategy = Cooperator()

    def update(self, other_move: Moves, round: None | int = None) -> None:
        if other_move == Moves.cheat:
            self._strategy = Cheater()


class MyPlayer(Player):
    def __init__(self, *, matches: None | int = None) -> None:
        super().__init__(matches=matches)
        self._strategies = [Cooperator(), Cheater()]
        self._strategy = choice(self._strategies)

    def move(self, other: None | Moves = None, round: None | int = None) -> str:
        return self._strategy.move(other=other, round=round)

    def reset(self) -> None:
        self._strategy = choice(self._strategies)

    def update(self, other_move: Moves, round: None | int = None) -> None:
        if other_move == Moves.cheat:
            self._strategy = Cheater()
        else:
            strategy = choice(self._strategies)
            self._strategy = strategy
        if self._matches and (round + 1) == self._matches:
            self._strategy = Cheater()
