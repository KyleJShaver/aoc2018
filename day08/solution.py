from common import getinput, bothparts, noop
from pathlib import Path
from os import sep
from uuid import uuid4
from typing import Set, List
from functools import reduce

DIR = str(Path(__file__).parent) + sep


class Node:
    __slots__ = ["id", "childcount", "metacount", "children", "metadata"]

    def __init__(self, childcount: int, metacount: int) -> None:
        self.id: str = str(uuid4())
        self.childcount: int = childcount
        self.metacount: int = metacount
        self.children: List["Node"] = list()
        self.metadata: List[int] = list()

    def addchild(self, node: "Node") -> bool:
        """
        Add a node to children and decrement childcount
        Return True if there is an available spot, False if the node can not accept more children
        """
        if self.childcount == 0:
            return False
        self.children.append(node)
        self.childcount -= 1
        return True

    def addmetadata(self, metadata: int) -> bool:
        """
        Add a metadata int to metadata and decrement metacount
        Return True if there is an available spot, False if the node can not accept more metadata
        """
        if self.metacount == 0:
            return False
        self.metadata.append(metadata)
        self.metacount -= 1
        return True

    def value(self) -> int:
        """ Return the sum of metadata """
        return reduce(lambda a, b: a + b, self.metadata)

    def childvalue(self) -> int:
        """ Return the value if no children, else return the value of children at indices given in metadata """
        if len(self.children) == 0:
            return self.value()
        childsum: int = 0
        for pos in self.metadata:
            if pos > len(self.children):
                continue
            childsum += self.children[pos - 1].childvalue()
        return childsum


def getnodes(data: str = None) -> List[Node]:
    """ Return a list of Nodes from provided data or input.txt """
    rawnodes: str = getinput(directory=DIR) if data is None else data
    nodenums: List[int] = list(map(int, rawnodes.split(" ")))
    nodestack: List[Node] = []
    nodes: List[Node] = []
    pos: int = 0
    while pos < len(nodenums):
        topnode: Node = None
        while topnode is None and len(nodestack) > 0:
            topnode: Node = nodestack[len(nodestack) - 1]
            if topnode.childcount == 0:
                while topnode.metacount > 0:
                    topnode.addmetadata(nodenums[pos])
                    pos += 1
                nodestack.pop()
                topnode = None
        if pos >= len(nodenums):
            break
        newnode: Node = Node(nodenums[pos], nodenums[pos + 1])
        nodes.append(newnode)
        nodestack.append(newnode)
        pos += 2
        if topnode is not None:
            topnode.addchild(newnode)
    return nodes


def part1(data: str = None) -> int:
    """ Return the sum of the values of the Nodes """
    nodes: List[Node] = getnodes(data)
    metasum: int = 0
    for node in nodes:
        metasum += node.value()
    return metasum


def part2(data: str = None) -> int:
    """ Return the childvalue of the root node """
    nodes: List[Node] = getnodes(data)
    return nodes[0].childvalue()


if __name__ == '__main__':  # pragma: no cover
    bothparts(part1, part2)
    noop()
