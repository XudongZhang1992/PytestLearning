"""
Group multiple tests in a class
Date: 21/02/2020
Note:
    pytest -q test_class.py
"""

class TestClass:
    def test_one(self):
        x = 'this'
        assert "h" in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, "check")