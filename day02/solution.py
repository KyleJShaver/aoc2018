from common import getinput, bothparts, noop
from typing import List, Dict, Set
import re


class IDProfiler:
    __slots__ = ["hastwo", "hasthree", "rawstr"]

    def __init__(self, rawstr: str = "") -> None:
        self.rawstr: str = rawstr
        self.hastwo: bool = False
        self.hasthree: bool = False
        counts: Dict[str, int] = dict()
        for letter in rawstr:
            if letter not in counts:
                counts[letter] = 0
            counts[letter] += 1
        for key, val in counts.items():
            if val == 2:
                self.hastwo = True
            elif val == 3:
                self.hasthree = True

    def sharedletters(self, idprofiler: "IDProfiler") -> str:
        """ Return the shared in-order letters between self and idprofiler """
        shared: str = ""
        for i in range(len(self.rawstr)):
            if self.rawstr[i] is idprofiler.rawstr[i]:
                shared += self.rawstr[i]
        return shared


def getidlist(data: str = None) -> List[IDProfiler]:
    """ Return a list of IDProfilers from provided data or input.txt """
    boxids: str = getinput() if data is None else data
    idlist: List[IDProfiler] = list(map(IDProfiler, boxids.split("\n")))
    return idlist


def part1(data: str = None) -> int:
    """ Return the checksum """
    idlist: List[IDProfiler] = getidlist(data)
    hastwo: List[IDProfiler] = list(filter(lambda a: a.hastwo is True, idlist))
    hasthree: List[IDProfiler] = list(filter(lambda a: a.hasthree is True, idlist))
    return len(hastwo) * len(hasthree)


def part2(data: str = None) -> str:
    """ Return the shared letters between two in which there is only one discrepancy """
    idlist: List[IDProfiler] = getidlist(data)
    for i in range(len(idlist)):
        for j in range(i + 1, len(idlist)):
            shared: str = idlist[i].sharedletters(idlist[j])
            if len(shared) is len(idlist[i].rawstr) - 1:
                return shared


def minpart1(data: str = open("input.txt", "r").read()) -> int:
    """ Return the checksum (minified version of part1) """
    lines: List[str] = data.split("\n")
    sets: List[Set[str]] = list(map(lambda a: set(), range(len(lines[0]) + 1)))
    for i in range(ord("a"), ord("z") + 1):
        for line in lines:
            sets[len(re.findall(f"{chr(i)}", line))].add(line)
    return len(sets[2]) * len(sets[3])


def minpart2(d: str = open("input.txt", "r").read(), s: Set[str] = None, a: int = 0, b: int = 1, p: int = 0) -> str:
    """
    Return the shared letters between two in which there is only one discrepancy
    (minified version of part2) (long runtime)
    """
    seen: Set[str] = s if s is not None else set()
    lines: List[str] = d.split("\n")
    if p >= len(lines[a]) or b >= len(lines) or f"{a}-{b}-{p}" in seen:
        return ""
    seen.add(f"{a}-{b}-{p}")
    if lines[a][:p] + lines[a][p + 1:] == lines[b][:p] + lines[b][p + 1:]:
        return lines[a][:p] + lines[a][p + 1:]
    return max(minpart2(d, seen, a, b + 1, p), minpart2(d, seen, a + 1, b + 1, p), minpart2(d, seen, a, b, p + 1))


if __name__ == '__main__':
    bothparts(part1, part2)
    noop()
