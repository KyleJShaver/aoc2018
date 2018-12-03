from typing import Callable
import time


def getinput(filename: str = "input.txt", directory: str = "") -> str:
    """ Return the contents of the input file as a str """
    with open(directory + filename, "r") as data:
        return data.read()


def bothparts(part1: Callable, part2: Callable) -> None:  # pragma: no cover
    """ Calls the provided functions with no arguments """
    start: float = time.time()
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
    end: float = time.time()
    print("\nRan in {:.4f} seconds".format(end - start))
