from common import getinput, bothparts, noop
from typing import List, Set
from functools import reduce


def getintchanges() -> List[int]:
    """ Return a list of integers from the input """
    data: str = getinput()
    strchanges: List[str] = data.split("\n")
    intchanges: List[int] = list(map(int, strchanges))
    return intchanges


def part1(data: List[int] = None) -> int:
    """ Return the sum of all elements of the input list """
    intchanges: List[int] = getintchanges() if data is None else data
    netchange: int = reduce(lambda a, b: a + b, intchanges)
    return netchange


def part2(data: List[int] = None) -> int:
    """ Return the first number to be visited twice, looping permanently to find it """
    intchanges: List[int] = getintchanges() if data is None else data
    runningfreq: int = 0
    freqset: Set[int] = {runningfreq}
    pos: int = 0
    while True:
        runningfreq += intchanges[pos]
        if runningfreq in freqset:
            return runningfreq
        freqset.add(runningfreq)
        pos = (pos + 1) % len(intchanges)


def minpart1(data: List[int]=list(map(int, open("input.txt", "r").read().split("\n")))) -> int:
    """ Return the sum of all elements of the input list (minified version of part1) """
    return reduce(lambda a, b: a + b, data)


def minpart2(data: List[int]=list(map(int, open("input.txt", "r").read().split("\n"))), pos=0, curr=0) -> int:
    """
    Return the first number to be visited twice, looping permanently to find it
    (minified version of part2)
    """
    s: Set[int] = {0}
    while True:
        curr += data[pos]
        if curr in s:
            return curr
        s.add(curr)
        pos = (pos + 1) % len(data)

if __name__ == '__main__':
    bothparts(part1, part2)
    noop()
