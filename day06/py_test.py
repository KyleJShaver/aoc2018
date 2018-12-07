from day06 import part1, part2


def test_part1() -> None:
    funcs = [part1]
    for func in funcs:
        # Provided examples
        assert func("1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9") == 17

        # Personal Input
        assert func() == 3660


def test_part2() -> None:
    funcs = [part2]
    for func in funcs:
        # Provided example
        assert func("1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9") is None

        # Personal Input
        assert func() is None
