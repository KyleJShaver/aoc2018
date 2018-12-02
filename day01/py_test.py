from day01 import part1, part2, minpart1, minpart2


def test_part1() -> None:
    funcs = [part1, minpart1]
    for func in funcs:
        # Provided examples
        assert func([1, -2, 3, 1]) == 3
        assert func([1, 1, 1]) == 3
        assert func([1, 1, -2]) == 0
        assert func([-1, -2, -3]) == -6

        # Personal Input
        assert func() == 538


def test_part2() -> None:
    funcs = [part2, minpart2]
    for func in funcs:
        # Provided examples
        assert func([1, -2, 3, 1]) == 2
        assert func([1, -1]) == 0
        assert func([3, 3, 4, -2, -4]) == 10
        assert func([-6, 3, 8, 5, -6]) == 5
        assert func([7, 7, -2, -7, -4]) == 14

        # Personal Input
        assert func() == 77271
