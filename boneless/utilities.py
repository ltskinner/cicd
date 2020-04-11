
import os

from datetime import datetime

import logging
from logging.handlers import HTTPHandler
from logging import FileHandler

import logging
logger = logging.getLogger()


class CustomHandler(FileHandler):

    def emit(self, record):
        """
        Overwrite .emit() if you need your logger to do something special
        Else, it will perform default behavior from inherited class

        # Review bedrock .emit()
        https://github.com/python/cpython/blob/3.8/Lib/logging/__init__.py#L1174
        # Which calls:
        https://github.com/python/cpython/blob/3.8/Lib/logging/__init__.py#L1069

        and uses `self.format(record)`
        """
        logging.FileHandler.emit(self, record)

        # payload = self.format(record)
        # return payload  # for HTTPHandler


class CustomFormatter(logging.Formatter):
    def format(self, record):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        custom_message = ' '.join([
            timestamp,
            'print() LOGGING from boneless.utilities.CustomHandler.emit():',
            str(super(CustomFormatter, self).format(record)),
        ])
        return custom_message


def get_env_name():
    if 'DEV_TEST_PROD' in os.environ.keys():
        env_name = os.environ['DEV_TEST_PROD']
    else:
        env_name = 'PROD'

    return env_name
