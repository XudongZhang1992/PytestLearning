"""
Assert that a certain exception is raised.
Date: 21/02/2020
Note:
    with statement is good.
    https://docs.python.org/2.5/whatsnew/pep-343.html
"""

import pytest

def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
