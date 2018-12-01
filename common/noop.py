from typing import Callable


def noop() -> Callable[[], None]:
    """
    A hastily written clone of Noop3:
    https://github.com/sindresorhus/noop3
    """
    return lambda: None
