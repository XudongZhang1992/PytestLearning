"""
Request a unique temporary directory for functional tests.
Date: 21/02/2020
Note:
    pytest provides Builtin fixtures/function arguments to request arbitrary resources, like a unique temporary directory:
    https://docs.pytest.org/en/latest/builtin.html
    
    pytest --fixtures  # shows bulitin and custom fixtures.

    tmpdir:
        Return a temporary directory path object
        which is unique to each test function invocation,
        created as a sub directory of the base temporary
        directory.
    
    pytest -q test_tmpdir.py
"""

def test_needsfiles(tmpdir):
    print(tmpdir)   # tmpdir is a builtin fixture of pytest
    assert 0