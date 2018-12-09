from common import getinput, bothparts, noop
from pathlib import Path
from os import sep
from typing import Tuple, List, Match, AnyStr
from re import match

DIR = str(Path(__file__).parent) + sep


class Node:
    __slots__ = ["value", "prev", "next"]

    def __init__(self, value: int):
        self.value: int = value
        self.prev: "Node" = None
        self.next: "Node" = None


def getgame(data: str = None) -> Tuple[List[int], int]:
    """ Return a str from provided data or input.txt """
    gamedef: str = getinput(directory=DIR) if data is None else data
    gamecomps:Match[AnyStr] = match(r'([0-9]+)[a-z\;\s]+([0-9]+)', gamedef)
    scored: List[int] = []
    for _ in range(0, int(gamecomps.group(1))):
        scored.append(0)
    return scored, int(gamecomps.group(2))


def playtomax(data: str = None, multiplier: int = 1):
    """
    Return the scores of the game
    :param data: the input data to define the game. If none is given, input.txt is used
    :param multiplier: the factor to multiply the max marble value by
    :return: a list of the scores of the players for the game
    """
    scores: List[int] = None
    maxval: int = 0
    scores, maxval = getgame(data)
    maxval *= multiplier

    # add 0 and 1 to get the ball rolling
    node: Node = Node(0)
    onenode = Node(1)
    node.next = onenode
    node.next.prev = node
    onenode.next = node
    onenode.next.prev = onenode
    node = node.next

    cplayer: int = 1
    c23 = 2
    for val in range(2, maxval + 1):
        percentcomplete = val / maxval
        if c23 == 23:
            for _ in range(0, 7):
                node = node.prev
            scores[cplayer] += node.value
            node.next.prev = node.prev
            node.prev.next = node.next
            node = node.next
            scores[cplayer] += val
            c23 = 0
        else:
            newnode = Node(val)
            for _ in range(0, 2):
                node = node.next
            newnode.next = node
            newnode.prev = node.prev
            node.prev = newnode
            newnode.prev.next = newnode
            node = newnode
        cplayer = (cplayer + 1) % len(scores)
        c23 += 1
    return scores


def part1(data: str = None) -> int:
    """
    Return the highest score for the game
    :param data: the input data to define the game. If none is given, input.txt is used
    :return:
    """
    return max(playtomax(data))


def part2(data: str = None):
    """
    Return the highest score for the game where max marble value is * 100
    :param data: the input data to define the game. If none is given, input.txt is used
    :return: the highest score for the game where max marble value is * 100
    """
    return max(playtomax(data, 100))


if __name__ == '__main__':  # pragma: no cover
    bothparts(part1, part2)
    noop()
