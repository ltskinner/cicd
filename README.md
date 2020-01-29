# cicd

Test ground for CICD tools

## File structure

```
/project
    /tests
        /unit
            __init__.py
        /integration
            /fixtures
                db_sample.py
            __init__.py
        __init__.py             # required to ensure `unittest discover` recurses
    __init__.py
    boneless.py
/hooks
    pre-commit
.coveragerc
.gitignore
MANIFEST.ini                    # required so requirements.txt is properly read by setup.py
README.md
requirements.txt
setup.py
tox.ini
```

## Executing Tests

```
# Unit Tests

$ python -m unittest discover -s boneless/tests/unit
```

```
# Integration Tests

$ python -m unittest discover -s boneless/tests/integration
```

## coverage

* See `.coveragerc`

```
# Full test suite (unit + integration)

$ coverage run -m unittest discover
$ coverage report -m
$ coverage html
```
