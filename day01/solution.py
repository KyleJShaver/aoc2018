from common import getinput, bothparts
from typing import List, Set
from functools import reduce


def getintchanges() -> List[int]:
    """ Return a list of integers from the input """
    data: str = getinput()
    strchanges: List[str] = data.split("\n", -1)
    intchanges: List[int] = list(map(int, strchanges))
    return intchanges


def part1(inlist: List[int] = None) -> int:
    """ Return the sum of all elements of the input list """
    intchanges: List[int] = getintchanges() if inlist is None else inlist
    netchange: int = reduce(lambda a, b: a + b, intchanges)
    return netchange


def part2(inlist: List[int] = None) -> int:
    """ Return the first number to be visited twice, looping permanently to find it """
    intchanges: List[int] = getintchanges() if inlist is None else inlist
    runningfreq: int = 0
    freqset: Set[int] = {runningfreq}
    pos: int = 0
    while True:
        runningfreq += intchanges[pos]
        if runningfreq in freqset:
            return runningfreq
        freqset.add(runningfreq)
        pos = (pos + 1) % len(intchanges)


def minpart1() -> int:
    """ Return the sum of all elements of the input list (minified version of part1) """
    return reduce(lambda a, b: a + b, list(map(int, open("input.txt", "r").read().split("\n", -1))))


if __name__ == '__main__':
    bothparts(part1, part2)
