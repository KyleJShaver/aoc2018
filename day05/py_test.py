from day05 import part1, part2


def test_part1() -> None:
    funcs = [part1]
    for func in funcs:
        # Provided examples
        assert func("aA") == 0
        assert func("abBA") == 0
        assert func("abAB") == 4
        assert func("aabAAB") == 6
        assert func("dabAcCaCBAcCcaDA") == 10

        # Personal Input
        assert func() == 11814


def test_part2() -> None:
    funcs = [part2]
    for func in funcs:
        # Provided example
        assert func("dabAcCaCBAcCcaDA") == 4

        # Personal Input
        assert func() == 4282
