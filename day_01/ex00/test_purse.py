import unittest

import purse


# in the shell:
# `python3 -m unittest test_purse.py`
# or `python3 test_purse.py`


class TestPurse(unittest.TestCase):

    def test_an_empty_purse(self):
        self.assertEqual(purse.empty(), {})

    def test_add_ingot_to_an_empty_purse(self):
        purse_ = purse.empty()
        added = purse.add_ingot(purse_)
        answer = {purse.INGOTS: 1}

        self.assertEqual(purse_, {})
        self.assertEqual(added, answer)

    def test_add_ingot_with_no_side_effects(self):
        purse_ = purse.empty()
        purse_ = purse.add_ingot(purse_)

        result = purse.add_ingot(purse_)

        self.assertEqual(purse_, {purse.INGOTS: 1})
        self.assertEqual(result, {purse.INGOTS: 2})

    def test_get_ingot_from_an_empty_purse(self):
        with self.assertRaises(ValueError):
            purse.get_ingot(purse.empty())

    def test_add_get_add_empty_chain(self):
        result = purse.add_ingot(purse.get_ingot(purse.add_ingot(purse.empty())))

        self.assertEqual(result, {purse.INGOTS: 1})

    def test_purse_get_attribute(self):
        purse_ = purse.add_ingot(purse.empty())
        key_ = purse.INGOTS

        self.assertEqual(key_, "gold_ingots")
        self.assertEqual(purse_[key_], 1)


if __name__ == "__main__":
    unittest.main()
