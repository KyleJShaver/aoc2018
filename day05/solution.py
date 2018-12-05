from common import getinput, bothparts, noop
from pathlib import Path
from os import sep
from typing import Pattern, AnyStr
import re

DIR = str(Path(__file__).parent) + sep


def getpolymer(data: str = None) -> str:
    """ Return the polymer from provided data or input.txt """
    polymer: str = getinput(directory=DIR) if data is None else data
    return polymer


def react(polymerin: str) -> str:
    """ Return the fully reacted polymer result in all lowercase"""
    polymer: str = re.sub(r'([A-Z])', r'{\1}', polymerin).lower()
    r: Pattern[AnyStr] = r'(([a-z])\{\2\})|(\{([a-z])\}\4)'
    while re.search(r, polymer) is not None:
        polymer = re.sub(r, "", polymer)
    polymer = re.sub("[\{\}]", "", polymer)
    return polymer


def part1(data: str = None) -> int:
    """ Return the number of unmatched units after all chain reactions """
    polymer: str = getpolymer(data)
    return len(react(polymer))


def part2(data: str = None) -> int:
    """ Return length of shortest chain reaction after removing all of a single letter """
    polymer: str = getpolymer(data)
    minlength: int = len(polymer)
    for asciichar in range(ord("a"), ord("z") + 1):
        polymermut = re.sub(chr(asciichar), "", polymer, flags=re.IGNORECASE)
        minlength = min(minlength, len(react(polymermut)))
    return minlength


if __name__ == '__main__':  # pragma: no cover
    bothparts(part1, part2)
    noop()
