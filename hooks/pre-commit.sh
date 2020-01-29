#!/bin/sh

echo "i Executing unit tests"
python -m unittest discover -s cicd/tests/unit

if [[ $? = 0 ]]
then
    echo "> Unit tests PASSED"
else
    echo "> Unit tests FAILED"
    echo "!     Please remove DEFECTs and run TESTS before committing"
    exit 1
fi

# Needs to occur outside of if/then
echo "+     Commit APPROVED"
exit 0
