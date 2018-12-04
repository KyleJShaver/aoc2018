from common import getinput, bothparts, noop
from pathlib import Path
from os import sep
from typing import Dict, List, Set
from functools import reduce

DIR = str(Path(__file__).parent) + sep


class Time:

    def __init__(self, rawinput: str) -> None:
        self.rawinput: str = rawinput
        components: List[str] = rawinput.split(" ")
        self.date: str = components.pop(0).lstrip("[")
        datecomponents: List[str] = self.date.split("-")
        self.year: int = int(datecomponents[0])
        self.month: int = int(datecomponents[1])
        self.day: int = int(datecomponents[2])
        self.time: str = components.pop(0).rstrip("]")
        timecomponents: List[str] = self.time.split(":")
        self.hour: int = int(timecomponents[0])
        self.minute: int = int(timecomponents[1])

    def diffmins(self, time: "Time") -> Set[int]:
        minutes: Set[int] = set()
        for minute in range(self.minute, time.minute):
            minutes.add(minute)
        return minutes


class Guard:

    def __init__(self, rawinput: str) -> None:
        self.shiftstart: Time = Time(rawinput)
        components: List[str] = rawinput.split(" ")[3:]
        self.id: int = int(components.pop(0).lstrip("#"))
        self.asleep: bool = False
        self.sleeptime: Time = None
        self.asleepmins: List[Set[int]] = []
        self.mostasleepmin: int = -1

    def sleep(self, time: Time) -> None:
        if self.asleep is True:
            return self.wake(time)
        self.asleep: bool = True
        self.sleeptime: Time = time

    def wake(self, time: Time) -> None:
        self.asleep = False
        self.asleepmins.append(self.sleeptime.diffmins(time))
        self.sleeptime = None

    def totalminsasleep(self) -> int:
        totalasleep: int = 0
        for asleepmins in self.asleepmins:
            totalasleep += len(asleepmins)
        return totalasleep

    def asleepmincounts(self) -> List[int]:
        asleepcount: List[int] = []
        for _ in range(0, 60):
            asleepcount.append(0)
        for sleepmins in self.asleepmins:
            for sleepmin in sleepmins:
                asleepcount[sleepmin] += 1
        self.mostasleepmin = reduce(lambda a, b: a if a > b else b, asleepcount)
        return asleepcount


def isguard(line: str) -> bool:
    if "#" in line:
        return True
    return False


def getguards(data: str = None) -> List[Guard]:
    """ Return a str from provided data or input.txt """
    times: List[str] = (getinput(directory=DIR) if data is None else data).split("\n")
    times.sort()
    guardlookup: Dict[int, Guard] = {}
    guards: List[Guard] = []
    lastguard: Guard = None

    for timeline in times:
        if isguard(timeline):
            guard: Guard = Guard(timeline)
            if guard.id in guardlookup:
                guard = guardlookup[guard.id]
            else:
                guardlookup[guard.id] = guard
                guards.append(guard)
            lastguard = guard
        else:
            lastguard.sleep(Time(timeline))
    return guards


def part1(data: str = None):
    guards: List[Guard] = getguards(data)
    guard: Guard = reduce(lambda a, b: a if a.totalminsasleep() > b.totalminsasleep() else b, guards)
    asleepcount: List[int] = guard.asleepmincounts()
    mostfreqmin = reduce(lambda a, b: a if a > b else b, asleepcount)
    return guard.id * asleepcount.index(mostfreqmin)


def part2(data: str = None):
    guards: List[Guard] = getguards(data)
    for guard in guards:
        guard.asleepmincounts()
    guard = reduce(lambda a, b: a if a.mostasleepmin > b.mostasleepmin else b, guards)
    return guard.id * guard.asleepmincounts().index(guard.mostasleepmin)


if __name__ == '__main__':
    bothparts(part1, part2)
    noop()
