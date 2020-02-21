# PytestLearning
## Install pytest
```
pip install -U pytest
```

## Check version
```
pytest --version
```

## Usage of assert statement
https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement

## Calling pytest through ```python -m pytest [...]```
This is almost equivalent to invoking the command line script ```pytest [...]``` directly, except that calling via python will also add the current directory to ```sys.path```.

## Possible exit codes

**Exit code 0:**	All tests were collected and passed successfully  
**Exit code 1:**	Tests were collected and run but some of the tests failed  
**Exit code 2:**	Test execution was interrupted by the user  
**Exit code 3:**	Internal error happened while executing tests  
**Exit code 4:**	pytest command line usage error  
**Exit code 5:**	No tests were collected

They are represented by the ```_pytest.config.ExitCode``` enum. The exit codes being a part of the public API can be imported and accessed directly using:
```
from pytest import ExitCode
```

## Version, option names, environment variables
```
pytest --version   # shows where pytest was imported from
pytest --fixtures  # show available builtin function arguments
pytest -h | --help # show help on command line and config file options
```

## Stopping after the first (or N) failures
```
pytest -x           # stop after first failure
pytest --maxfail=2  # stop after two failures
```

## Specifying tests / selecting tests
**Run tests in a module**  
```
pytest test_mod.py
```
**Run tests in a directory**
```
pytest testing/
```
**Run tests by keyword expressions**
```
pytest -k "MyClass and not method"
```
This will run tests which contain names that match the given *string expression* (case-insensitive), which can include Python operators that use filenames, class names and function names as variables. The example above will run ```TestMyClass.test_something``` but not ```TestMyClass.test_method_simple```.

## Run tests by node IDs
To run a specific test within a module:
```
pytest test_mode.py::test_func
```
Another example specifying a test method in the command line:
```
pytest test_mod.py::TestClass::test_method
```
**Run tests by marker expressions**
```
pytest -m slow
```
Will run all tests which are decorated with the ```@pytest.mark.slow decorator```.
**Run tests from packages**
```
pytest --pyargs pkg.testing
```
This will import ```pkg.testing``` and use its filesystem location to find and run tests from.

## Modifying Python trackback printing
```Python
pytest --showlocals # show local variables in tracebacks
pytest -l           # show local variables (shortcut)

pytest --tb=auto    # (default) 'long' tracebacks for the first and last
                     # entry, but 'short' style for the other entries
pytest --tb=long    # exhaustive, informative traceback formatting
pytest --tb=short   # shorter traceback format
pytest --tb=line    # only one line per failure
pytest --tb=native  # Python standard library formatting
pytest --tb=no      # no traceback at all
```
The --full-trace causes very long traces to be printed on error (longer than ```--tb=long```). It also ensures that a stack trace is printed on **KeyboardInterrupt** (Ctrl+C). This is very useful if the tests are taking too long and you interrupt them with Ctrl+C to find out where the tests are hanging. By default no output will be shown (because KeyboardInterrupt is caught by pytest). By using this option you make sure a trace is shown.

## Detailed summary report
The ```-r``` flag can be used to display a “short test summary info” at the end of the test session, making it easy in large test suites to get a clear picture of all failures, skips, xfails, etc.
It defaults to ```fE``` to list failures and errors.
Example:
```Python
# content of test_example.py
import pytest


@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass
```
```Shell
$ pytest -ra
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-5.x.y, py-1.x.y, pluggy-0.x.y
cachedir: $PYTHON_PREFIX/.pytest_cache
rootdir: $REGENDOC_TMPDIR
collected 6 items

test_example.py .FEsxX                                               [100%]

================================== ERRORS ==================================
_______________________ ERROR at setup of test_error _______________________

    @pytest.fixture
    def error_fixture():
>       assert 0
E       assert 0

test_example.py:6: AssertionError
================================= FAILURES =================================
________________________________ test_fail _________________________________

    def test_fail():
>       assert 0
E       assert 0

test_example.py:14: AssertionError
========================= short test summary info ==========================
SKIPPED [1] $REGENDOC_TMPDIR/test_example.py:22: skipping this test
XFAIL test_example.py::test_xfail
  reason: xfailing this test
XPASS test_example.py::test_xpass always xfail
ERROR test_example.py::test_error - assert 0
FAILED test_example.py::test_fail - assert 0
== 1 failed, 1 passed, 1 skipped, 1 xfailed, 1 xpassed, 1 error in 0.12s ===
```
The ```-r``` options accepts a number of characters after it, with a used above meaning “all except passes”.
Here is the full list of available characters that can be used:
* ```f``` - failed
* ```E``` - error
* ```s``` - skipped
* ```x``` - xfailed
* ```X``` - xpassed
* ```p``` - passed* 
* ```P``` - passed with output  

Special characters for (de)selection of groups:

* ```a``` - all except pP
* ```A``` - all
* ```N``` - none, this can be used to display nothing (since fE is the default)

More than one character can be used, so for example to only see failed and skipped tests, you can execute:
```Shell
$ pytest -rfs
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-5.x.y, py-1.x.y, pluggy-0.x.y
cachedir: $PYTHON_PREFIX/.pytest_cache
rootdir: $REGENDOC_TMPDIR
collected 6 items

test_example.py .FEsxX                                               [100%]

================================== ERRORS ==================================
_______________________ ERROR at setup of test_error _______________________

    @pytest.fixture
    def error_fixture():
>       assert 0
E       assert 0

test_example.py:6: AssertionError
================================= FAILURES =================================
________________________________ test_fail _________________________________

    def test_fail():
>       assert 0
E       assert 0

test_example.py:14: AssertionError
========================= short test summary info ==========================
FAILED test_example.py::test_fail - assert 0
SKIPPED [1] $REGENDOC_TMPDIR/test_example.py:22: skipping this test
== 1 failed, 1 passed, 1 skipped, 1 xfailed, 1 xpassed, 1 error in 0.12s ===
```
Using ```p``` lists the passing tests, whilst ```P``` adds an extra section “PASSES” with those tests that passed but had captured output:
```Shell
$ pytest -rpP
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-5.x.y, py-1.x.y, pluggy-0.x.y
cachedir: $PYTHON_PREFIX/.pytest_cache
rootdir: $REGENDOC_TMPDIR
collected 6 items

test_example.py .FEsxX                                               [100%]

================================== ERRORS ==================================
_______________________ ERROR at setup of test_error _______________________

    @pytest.fixture
    def error_fixture():
>       assert 0
E       assert 0

test_example.py:6: AssertionError
================================= FAILURES =================================
________________________________ test_fail _________________________________

    def test_fail():
>       assert 0
E       assert 0

test_example.py:14: AssertionError
================================== PASSES ==================================
_________________________________ test_ok __________________________________
--------------------------- Captured stdout call ---------------------------
ok
========================= short test summary info ==========================
PASSED test_example.py::test_ok
== 1 failed, 1 passed, 1 skipped, 1 xfailed, 1 xpassed, 1 error in 0.12s ===
```

## Dropping to PDB (Python Debugger) at the start of a test
```
pytest --trace
```
(Never used before...)

## Setting breakpoints
To set a breakpoint in your code use the native Python ```import pdb; pdb.set_trace()``` call in your code and pytest automatically disables its output capture for that test.


