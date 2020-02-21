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

