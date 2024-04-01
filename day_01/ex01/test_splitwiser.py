import unittest
from copy import deepcopy

import purse
import splitwiser


# in the shell:
# `python3 -m unittest test_purse.py`
# or `python3 test_purse.py`


def _assert_diff_on_booty_split(
    booty: tuple[purse.PurseType, purse.PurseType, purse.PurseType]
) -> None:
    i1, i2, i3 = [p["gold_ingots"] for p in booty]

    assert abs(i1 - i2) <= 1
    assert abs(i1 - i3) <= 1
    assert abs(i2 - i3) <= 1


class TestSplitBooty(unittest.TestCase):

    def test_on_empty_purses(self):
        purses = [{}, {}, {}]
        answer = (
            {purse.PurseFields.GI: 0},
            {purse.PurseFields.GI: 0},
            {purse.PurseFields.GI: 0},
        )

        result = splitwiser.split_booty(*purses)

        self.assertEqual(result, answer)
        _assert_diff_on_booty_split(result)

    def test_on_equal_purses(self):
        purses = [
            {purse.PurseFields.GI: 1},
            {purse.PurseFields.GI: 1},
            {purse.PurseFields.GI: 1},
        ]
        answer = tuple(deepcopy(purses))

        result = splitwiser.split_booty(*purses)

        self.assertEqual(result, answer)
        _assert_diff_on_booty_split(result)

    def test_on_123_ingots_purses(self):
        purses = [
            {purse.PurseFields.GI: 1},
            {purse.PurseFields.GI: 2},
            {purse.PurseFields.GI: 3},
        ]
        answer = (
            {purse.PurseFields.GI: 2},
            {purse.PurseFields.GI: 2},
            {purse.PurseFields.GI: 2},
        )

        result = splitwiser.split_booty(*purses)

        self.assertEqual(result, answer)
        _assert_diff_on_booty_split(result)

    def test_on_apples_ingots_purses(self):
        purses = [
            {purse.PurseFields.GI: 3},
            {purse.PurseFields.GI: 2},
            {"apples": 10},
        ]
        answer = (
            {purse.PurseFields.GI: 2},
            {purse.PurseFields.GI: 2},
            {purse.PurseFields.GI: 1},
        )

        result = splitwiser.split_booty(*purses)
        result = tuple(
            sorted(result, key=lambda p: p[purse.PurseFields.GI], reverse=True)
        )

        self.assertEqual(result, answer)
        _assert_diff_on_booty_split(result)


if __name__ == "__main__":
    unittest.main()
