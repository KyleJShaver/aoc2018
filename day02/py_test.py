from day02 import part1, part2, minpart1, minpart2


def test_part1() -> None:
    funcs = [part1, minpart1]
    for func in funcs:
        # Provided example
        assert func("abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab") ==  12

        # Personal Input
        assert func() == 6175


def test_part2() -> None:
    funcs = [part2, minpart2]
    for func in funcs:
        # Provided example
        assert func("abcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz") == "fgij"

        # Personal Input
        assert func() == "asgwjcmzredihqoutcylvzinx"
