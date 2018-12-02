from common import getinput, bothparts, noop


def getval(data: str = None) -> str:
    """ Return a str from provided data or input.txt """
    val: str = getinput() if data is None else data
    return val


def part1():
    pass


def part2():
    pass


if __name__ == '__main__':
    bothparts(part1, part2)
    noop()
