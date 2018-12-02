from common import getinput, bothparts
from typing import List, Dict


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
        for j in range(len(idlist)):
            if j is i:
                continue
            shared: str = idlist[i].sharedletters(idlist[j])
            if len(shared) is len(idlist[i].rawstr) - 1:
                return shared


if __name__ == '__main__':
    bothparts(part1, part2)
