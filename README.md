# cicd

![](https://codebuild.us-east-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiWmZFUU9ZS1NtM1JIdVFYOG0yejBucmFxR2JOYVN0YVZUcTBzSW9ZWjI1K2VCUk1mbXNWQ2NBdUZZWjBLclAxOGxnRnZBRUc4U1c4d0lJdkVreC83MXU0PSIsIml2UGFyYW1ldGVyU3BlYyI6ImR2endXajBObVptcWl3c28iLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

(More badges at: [shields.io](shields.io))

Test ground for CICD tools

## File structure

```
/.vscode
    settings.json               # Note, this will just be local - not in source control
/hooks
    pre-commit                  # Will need to move these into the local `.git` folder
/lib
    banner.txt
/data
    /raw                        # House raw source data in /raw
    enriched.csv
/models
    model_weights.h5
/project
    /tests
        /unit
            __init__.py
        /integration
            /fixtures
                db_sample.py
            __init__.py
        __init__.py             # required to ensure `unittest discover` recurses
    /subpackage
        __init__.py
        submodule.py
    __init__.py
    boneless.py
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

## Test coverage

* See `.coveragerc`

```
# Full test suite (unit + integration)

$ coverage run -m unittest discover
$ coverage report -m
$ coverage html
```

## Bulding package

```
$ python setup.py sdist bdist_wheel
```

### [--> Full build to PyPi here](https://github.com/ltskinner/software-engineering/blob/master/python/PYPI.md)

## Naming Conventions

| Class | Instance | Conventions --> | | |
|-|-|-|-|-|
| **Project** | repos | Capitalized-With-Hyphens | OrNoSpaces | Git-Repositories |
| | packages | lowercase_underscores |
| | modules.py | lowercase_underscore | make_sure_are_unique.py |
| **Documentation** | MS Docs | Word_Documents.docx | PDF_Docs.pdf | Visio.vsdx |
| | .md | USE_CAPS_UNDERSCORES.md |
| | .drawio | DrawIO_Architecture.drawio | Capitalized, '_' |
| **/data** | use_dates_YYYY_MM_DD.csv |
| **/models** | use_dates_too_YYYY_MM_DD.h5 | version_models_v1.h5 |

## Sprint Board - Swimlanes

| Backlogs | | Design | | | | Implementation | | | Testing | | | Deployed |
|-|-|-|-|-|-|-|-|-|-|-|-|-|
| Project | Sprint | Problem Framing | In Progress | "Done" | Review | In Progress | "Done" | Review | In Progress | "Done" | Review | Deployed |
