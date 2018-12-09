from day09 import part1, part2


def test_part1() -> None:
    funcs = [part1]
    for func in funcs:
        # Provided examples
        assert func("10 players; last marble is worth 1618 points") == 8317
        assert func("13 players; last marble is worth 7999 points") == 146373
        assert func("17 players; last marble is worth 1104 points") == 2764
        assert func("21 players; last marble is worth 6111 points") == 54718
        assert func("30 players; last marble is worth 5807 points") == 37305

        # Personal Input
        assert func() == 405143


def test_part2() -> None:
    funcs = [part2]
    for func in funcs:
        # NO Provided example

        # Personal Input
        assert func() == 3411514667
