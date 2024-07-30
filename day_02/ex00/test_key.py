import unittest
from typing import ClassVar

import key


class TestKey(unittest.TestCase):
    # https://github.com/python/mypy/issues/8723?ysclid=lulpmmrzkd844337779
    key: ClassVar = None  # to please `mypy`

    @classmethod
    def setUpClass(cls):
        cls.key = key.Key()

    def test_getitem(self) -> None:
        parametrised = [
            (-1, 1),
            (0, 1),
            (4, 1),
            (44, 2),
            (404, 3),
            (4004, 4),
        ]
        for value, answer in parametrised:
            with self.subTest(key=value, ans=answer, msg="testing key == ans"):
                self.assertEqual(self.key[value], answer)

    def test_gt(self) -> None:
        upper_limit = 9000

        self.assertFalse(self.key > upper_limit, msg="key <= 9000")
        self.assertTrue(self.key > upper_limit + 1, msg="key > 9000")

    def test_len(self) -> None:
        length = len(self.key)
        answer = 1337

        self.assertEqual(length, answer)

    def test_passphrase(self) -> None:
        pass_phrase = self.key.passphrase
        answer = "zax2rulez"

        self.assertEqual(pass_phrase, answer)

    def test_str(self) -> None:
        cls_str = str(self.key)
        answer = "GeneralTsoKeycard"

        self.assertEqual(cls_str, answer)


if __name__ == "__main__":
    unittest.main()
