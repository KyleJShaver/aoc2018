from day08 import part1, part2, Node


def testimpossibleadds() -> None:
    childnode: Node = Node(0, 3)
    addnode: Node = Node(1, 1)
    assert childnode.addchild(addnode) is False
    metanode: Node = Node(3, 0)
    assert metanode.addmetadata(1) is False


def test_part1() -> None:
    funcs = [part1]
    for func in funcs:
        # Provided example
        assert func("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2") == 138

        # Personal Input
        assert func() == 41849


def test_part2() -> None:
    funcs = [part2]
    for func in funcs:
        # Provided example
        assert func("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2") == 66

        # Personal Input
        assert func() == 32487
