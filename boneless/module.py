
from .subpackage import sub_module_function


def module_function():
    print('printing from module.py')
    return True


def use_sub_module_function():
    print('accessing submodule')
    sub_module_function()
    return True


def test_read_from_lib():
    with open('lib/banner.txt') as f:
        contents = f.read()

    print('lib/banner.txt contents:')
    print(repr(contents))
    return contents
