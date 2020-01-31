# cicd

![](https://codebuild.us-east-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiWmZFUU9ZS1NtM1JIdVFYOG0yejBucmFxR2JOYVN0YVZUcTBzSW9ZWjI1K2VCUk1mbXNWQ2NBdUZZWjBLclAxOGxnRnZBRUc4U1c4d0lJdkVreC83MXU0PSIsIml2UGFyYW1ldGVyU3BlYyI6ImR2endXajBObVptcWl3c28iLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

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
