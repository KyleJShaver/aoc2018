from common.common import getinput, bothparts
from typing import List, Set
from functools import reduce


def getintchanges() -> List[int]:
    data: str = getinput()
    strchanges: List[str] = data.split("\n", -1)
    intchanges: List[int] = list(map(int, strchanges))
    return intchanges


def part1() -> int:
    intchanges: List[int] = getintchanges()
    netchange: int = reduce(lambda a, b: a + b, intchanges)
    return netchange


def part2() -> int:
    intchanges: List[int] = getintchanges()
    runningfreq: int = 0
    freqset: Set[int] = {runningfreq}
    pos: int = 0
    while True:
        runningfreq += intchanges[pos]
        if runningfreq in freqset:
            return runningfreq
        freqset.add(runningfreq)
        pos = (pos + 1) % len(intchanges)


bothparts(part1, part2)
