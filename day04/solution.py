from common import getinput, bothparts, noop
from pathlib import Path
from os import sep
from typing import Dict, List, Set, Tuple
from re import match
from functools import reduce

DIR = str(Path(__file__).parent) + sep


class Guard:
    __slots__ = ["id", "sleepmins", "sleepstart"]

    def __init__(self, timeline: str) -> None:
        rematch = match(".*#(\d+)", timeline)
        self.id = int(rematch.group(1))
        self.sleepmins: List[List[int]] = []
        self.sleepstart: int = -1

    def dosleep(self, timeline: str) -> None:
        """ Toggle Guard's sleep action, saving list of time spent asleep when toggled to wake up """
        minute: int = int(match(".*:(\d+)", timeline).group(1))
        if self.sleepstart < 0:
            self.sleepstart = minute
        else:
            self.sleepmins.append(list(range(self.sleepstart, minute)))
            self.sleepstart = -1

    def sleepduration(self) -> int:
        """ Return the total number of minutes spent asleep """
        duration: int = 0
        for minutes in self.sleepmins:
            duration += len(minutes)
        return duration

    def sleepmax(self) -> Tuple[int, int]:
        """ Return the count of the most frequent asleep minute and the most frequent asleep minute """
        frequencies: List[int] = []
        for _ in range(0, 60):
            frequencies.append(0)
        for sleepmins in self.sleepmins:
            for minute in sleepmins:
                frequencies[minute] += 1
        freqcount: int = max(frequencies)
        return freqcount, frequencies.index(freqcount)


def getguards(data: str = None) -> List[Guard]:
    """ Return a list of Guards from provided data or input.txt """
    times: List[str] = (getinput(directory=DIR) if data is None else data).split("\n")
    times.sort()
    guards: Dict[int, Guard] = dict()
    lastguard: Guard = None
    for timeline in times:
        if "#" in timeline:
            guard = Guard(timeline)
            if guard.id not in guards:
                guards[guard.id] = guard
            lastguard = guards[guard.id]
        else:
            lastguard.dosleep(timeline)
    return guards.values()


def part1(data: str = None) -> int:
    """ Return the Guard with the longest sleep time's id times the most frequent minute they are asleep """
    guards: List[Guard] = getguards(data)
    longestsleeper = reduce(lambda a, b: a if a.sleepduration() > b.sleepduration() else b, guards)
    return longestsleeper.id * longestsleeper.sleepmax()[1]


def part2(data: str = None) -> int:
    """ Return the Guard with the most consistent sleep minute's id times the most frequent minute they are asleep """
    guards: List[Guard] = getguards(data)
    consistentsleeper: Guard = reduce(lambda a, b: a if a.sleepmax()[0] > b.sleepmax()[0] else b, guards)
    return consistentsleeper.id * consistentsleeper.sleepmax()[1]


if __name__ == '__main__':  # pragma: no cover
    bothparts(part1, part2)
    noop()
