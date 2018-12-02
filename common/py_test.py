from common import noop

def test_noop():
    assert noop()() is None