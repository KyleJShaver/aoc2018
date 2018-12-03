from common import getinput, bothparts, noop
from pathlib import Path
from os import sep
from typing import List, Set

DIR = str(Path(__file__).parent) + sep


class Rectangle:
    __slots__ = ["id", "x", "y", "width", "height"]

    def __init__(self, description: str = "#0 @ 0,0: 1x1") -> None:
        components: List[str] = description.split(" ")
        self.id: int = int(components.pop(0)[1:])
        _ = components.pop(0)  # eliminate the @
        coords: List[int] = list(map(int, components.pop(0).rstrip(":").split(",")))
        self.x: int = coords[0]
        self.y: int = coords[1]
        size: List[int] = list(map(int, components.pop(0).split("x")))
        self.width: int = size[0]
        self.height: int = size[1]

    def claimedcoords(self) -> Set[str]:
        """ Return the set of all squares in this claim """
        touched: Set[str] = set()
        for x in range(self.x, self.x + self.width):
            for y in range(self.y, self.y + self.height):
                touched.add(f"{x},{y}")
        return touched


def getrectangles(data: str = None) -> List[Rectangle]:
    """ Return a list of Rectangles from provided data or input.txt """
    allrects: str = getinput(directory=DIR) if data is None else data
    rects: List[Rectangle] = list(map(Rectangle, allrects.split("\n")))
    return rects


def claimsoverlaps(data: str = None) -> Set[str]:
    """ Return a set of square claims that overlap """
    rects: List[Rectangle] = getrectangles(data)
    claimed: Set[str] = set()
    overlaps: Set[str] = set()
    for rect in rects:
        recttouched: Set[str] = rect.claimedcoords()
        overlaps.update(claimed.intersection(recttouched))
        claimed.update(recttouched)
    return overlaps


def part1(data: str = None) -> int:
    """ Return the number of overlapped claim squares """
    overlaps: Set[str] = claimsoverlaps(data)
    return len(overlaps)


def part2(data: str = None) -> int:
    """ Return the id of the one claim that does not overlap any others """
    overlaps: Set[str] = claimsoverlaps(data)
    rects: List[Rectangle] = getrectangles(data)
    for rect in rects:
        intersect: Set[str] = overlaps.intersection(rect.claimedcoords())
        if len(intersect) == 0:
            return rect.id


if __name__ == '__main__':  # pragma: no cover
    bothparts(part1, part2)
    noop()
