"""
This script registers your project in pypi.

when registering via twine(1) you need to:
- full clean
- build wheel using setup.py
- twine register
- full clean
This method works, if you register twice it is ok.
You just need to do it once...:)

when registering via setup.py you need to:
- full clean
- python setup.py register -r pypi
- full clean
registering the same package many times works.
You just need to do it once...:)

References:
- https://packaging.python.org/distributing/

TODO:
- check if I'm already registered and don't register if that is the case.
"""

import pypitools.common
import os

from pypitools import common
from pypitools.common import ConfigData


def register_by_setup(config: ConfigData) -> None:
    pypitools.common.check_call_no_output([
        '{}'.format(config.python),
        'setup.py',
        'register',
        '-r',
        'pypi',
    ])


def register_by_twine(config: ConfigData) -> None:
    pypitools.common.check_call_no_output([
        '{}'.format(config.python),
        'setup.py',
        'bdist_wheel',
    ])

    # at this point there should be only one file in the 'dist' folder
    file_list = list(os.listdir('dist'))
    assert len(file_list) == 1
    filename = file_list[0]
    full_filename = os.path.join('dist', filename)
    pypitools.common.check_call_no_output([
        'twine',
        'register',
        full_filename,
    ])


def main():
    common.setup_main()
    config = common.read_config()
    pypitools.common.git_clean_full()
    try:
        if config.register_method == "twine":
            register_by_twine(config)
        if config.register_method == "setup":
            register_by_setup(config)
    finally:
        pypitools.common.git_clean_full()
