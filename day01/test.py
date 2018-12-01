import unittest
from day01 import part1, part2, minpart1, minpart2


class TestDay01(unittest.TestCase):

    def test_part1(self) -> None:
        funcs = [part1, minpart1]
        for func in funcs:
            # Provided examples
            self.assertEqual(func([1, -2, 3, 1]), 3)
            self.assertEqual(func([1, 1, 1]), 3)
            self.assertEqual(func([1, 1, -2]), 0)
            self.assertEqual(func([-1, -2, -3]), -6)

            # Personal Input
            self.assertEqual(func(), 538)

    def test_part2(self) -> None:
        funcs = [part2, minpart2]
        for func in funcs:
            # Provided examples
            self.assertEqual(func([1, -2, 3, 1]), 2)
            self.assertEqual(func([1, -1]), 0)
            self.assertEqual(func([3, 3, 4, -2, -4]), 10)
            self.assertEqual(func([-6, 3, 8, 5, -6]), 5)
            self.assertEqual(func([7, 7, -2, -7, -4]), 14)

            # Personal Input
            self.assertEqual(func(), 77271)
