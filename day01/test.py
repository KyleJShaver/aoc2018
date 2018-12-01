import unittest
from day01 import part1, part2


class TestDay01(unittest.TestCase):

    def test_part1(self) -> None:
        # Provided examples
        self.assertEqual(part1([1, -2, 3, 1]), 3)
        self.assertEqual(part1([1, 1, 1]), 3)
        self.assertEqual(part1([1, 1, -2]), 0)
        self.assertEqual(part1([-1, -2, -3]), -6)

        # Personal Input
        self.assertEqual(part1(), 538)

    def test_part2(self) -> None:
        # Provided examples
        self.assertEqual(part2([1, -2, 3, 1]), 2)
        self.assertEqual(part2([1, -1]), 0)
        self.assertEqual(part2([3, 3, 4, -2, -4]), 10)
        self.assertEqual(part2([-6, 3, 8, 5, -6]), 5)
        self.assertEqual(part2([7, 7, -2, -7, -4]), 14)

        # Personal Input
        self.assertEqual(part2(), 77271)
