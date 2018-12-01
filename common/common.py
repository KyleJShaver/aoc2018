from typing import Callable


def getinput(filename: str = "input.txt") -> str:
    """ Return the contents of the input file as a str """
    with open(filename, "r") as data:
        return data.read()


def bothparts(part1: Callable, part2: Callable) -> None:
    """ Calls the provided functions with no arguments """
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
