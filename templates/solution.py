from common import getinput, bothparts, noop
from pathlib import Path
from os import sep

DIR = str(Path(__file__).parent) + sep


def getval(data: str = None) -> str:
    """ Return a str from provided data or input.txt """
    val: str = getinput(directory=DIR) if data is None else data
    return val


def part1(data: str = None):
    pass


def part2(data: str = None):
    pass


if __name__ == '__main__':  # pragma: no cover
    bothparts(part1, part2)
    noop()
