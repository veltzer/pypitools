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


def register_by_setup():
    pypitools.common.check_call_no_output([
        'python',
        'setup.py',
        'register',
        '-r',
        'pypi',
    ])


def register_by_twine():
    pypitools.common.check_call_no_output([
        'python3',
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
    do_use_setup = False
    do_use_twine = True

    pypitools.common.git_clean_full()
    try:
        if do_use_setup:
            register_by_setup()
        if do_use_twine:
            register_by_twine()
    finally:
        pypitools.common.git_clean_full()
