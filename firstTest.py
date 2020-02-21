"""
My first test using pytest
Date: 21/02/2020
Note:
    Using "pytest firstTest.py to execute the test function.
    The error report will show the assertion violation.
    'assert' usage learnt.
    Assert statement in python3:
        https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
"""

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5