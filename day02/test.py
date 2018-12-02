import unittest
from day02 import part1, part2


class TestDay02(unittest.TestCase):

    def test_part1(self) -> None:
        funcs = [part1]
        for func in funcs:
            # Provided example
            self.assertEqual(func("abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab"), 12)

            # Personal Input
            self.assertEqual(func(), 6175)

    def test_part2(self) -> None:
        funcs = [part2]
        for func in funcs:
            # Provided example
            self.assertEqual(func("abcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz"), "fgij")

            # Personal Input
            self.assertEqual(func(), "asgwjcmzredihqoutcylvzinx")
