
import os


def get_env_name():
    if 'DEV_TEST_PROD' in os.environ.keys():
        env_name = os.environ['DEV_TEST_PROD']
    else:
        env_name = 'PROD'

    return env_name
