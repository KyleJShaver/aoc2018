from day03 import part1, part2


def test_part1() -> None:
    funcs = [part1]
    for func in funcs:
        # Provided example
        assert func("#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2") == 4

        # Personal Input
        assert func() == 121259


def test_part2() -> None:
    funcs = [part2]
    for func in funcs:
        # Provided example
        assert func("#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2") == 3

        # Personal Input
        assert func() == 239
