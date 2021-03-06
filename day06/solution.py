from common import getinput, bothparts, noop
from pathlib import Path
from os import sep
from typing import List, Set, Dict, Tuple
from operator import attrgetter
import uuid

DIR = str(Path(__file__).parent) + sep


class Point:
    __slots__ = ["x", "y", "id"]

    def __init__(self, rawstr: str) -> None:
        coords: List[int] = list(map(int, rawstr.split(", ")))
        self.x: int = coords[0]
        self.y: int = coords[1]
        self.id: str = str(uuid.uuid4())

    def manhattan(self, p: "Point") -> int:
        """ Return the manhattan distance from this point to any other """
        return abs(self.x - p.x) + abs(self.y - p.y)


def getpoints(data: str = None) -> List[Point]:
    """ Return a list of Points from provided data or input.txt """
    pointsdata: List[str] = (getinput(directory=DIR) if data is None else data).split("\n")
    pointslist: List[Point] = []
    for point in pointsdata:
        pointslist.append(Point(point))
    return pointslist


def sortpoints(points: List[Point], sortx: bool = True) -> List[Point]:
    """ Return the points list sorted by x if sortx is True or y if sortx is False """
    return sorted(points, key=attrgetter("x" if sortx is True else "y"))


def spacemap(points: List[Point], extrapad: bool = False) -> List[List[str]]:
    """ Return a 2D list where the indices are the coordinate and the value is the id of the closest point """
    maxx: int = points[len(points) - 1].x
    minx: int = points[0].x
    points = sortpoints(points, False)
    maxy: int = points[len(points) - 1].y
    miny: int = points[0].y
    space: List[List[str]] = []
    padding: int = 1 if extrapad is False else 100
    for x in range(minx - padding, maxx + padding):
        row: List[str] = []
        for y in range(miny - padding, maxy + padding):
            currpoint: Point = Point(f'{x}, {y}')
            closestdist: int = maxx + maxy
            closestnode: Point = None
            pointdist: int = 0
            for point in points:
                manhattan: int = currpoint.manhattan(point)
                if manhattan < closestdist:
                    closestdist = manhattan
                    closestnode = point
                elif manhattan == closestdist:
                    closestnode = None
                pointdist += manhattan
            row.append(("" if closestnode is None else closestnode.id) + f'{pointdist}')
        space.append(row)
    return space


def infinitepoints(space: List[List[str]]) -> Set[str]:
    """ Return the ids  """
    infinite: Set[str] = set()
    for x in [0, len(space) - 1]:
        for y in range(0, len(space[0])):
            infinite.add(space[x][y][:36])
    for x in range(0, len(space)):
        for y in [0, len(space[0]) - 1]:
            infinite.add(space[x][y][:36])
    return infinite


def part1(data: str = None) -> int:
    """ Return the largest non-infinite area """
    points: List[Point] = sortpoints(getpoints(data))
    space: List[List[str]] = spacemap(points)
    infinite: Set[str] = infinitepoints(space)
    count: Dict[str, int] = dict()
    for x in range(0, len(space)):
        for y in range(0, len(space[0])):
            point = space[x][y]
            pointid = point[:36]
            if len(pointid) < 36 or pointid in infinite:
                continue
            if pointid not in count:
                count[pointid] = 0
            count[pointid] += 1
    return max(count.values())


def part2(data: str = None, maxdist: int = 10000):
    """ Return number of points with max distance from all points < maxdist """
    points: List[Point] = sortpoints(getpoints(data))
    space: List[List[str]] = spacemap(points, extrapad=True)
    safe: int = 0
    for x in range(0, len(space)):
        for y in range(0, len(space[0])):
            point = space[x][y]
            totaldist = int(point) if len(point) < 36 else int(point[36:])
            if totaldist < maxdist:
                safe += 1
    return safe


if __name__ == '__main__':  # pragma: no cover
    bothparts(part1, part2)
    noop()
