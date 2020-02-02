
from .subpackage import sub_module_function

import logging
logger = logging.getLogger()


def module_function():
    logger.info('printing from module.py')
    return True


def use_sub_module_function():
    logger.info('accessing submodule')
    sub_module_function()
    return True


def test_read_from_lib():
    with open('lib/banner.txt') as f:
        contents = f.read()

    logger.info('lib/banner.txt contents:')
    logger.info(repr(contents))
    return contents
