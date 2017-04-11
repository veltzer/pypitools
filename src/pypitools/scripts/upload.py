"""
This script uploads your module to where ever you configure it.
It's default is to upload to pypi but you can override by putting
a pypi.cnf file in the root of your source tree.


It does the following:
- clean
- setup.py sdist
- twine upload
- clean again

Notes:
- This script could be done via setuptools using the following:
$ python3 setup.py sdist upload -r pypi --identity="Mark Veltzer" --sign
but this has bad security implications as it sends user and password plain text.
- we use twine(1) to upload the package.
On ubuntu twine(1) is from the 'twine' official ubuntu package.

References:
- https://pypi.python.org/pypi/twine
- https://python-packaging-user-guide.readthedocs.org/en/latest/index.html
- http://peterdowns.com/posts/first-time-with-pypi.html
"""
import configparser
import os
import os.path

import click
from pyfakeuse.pyfakeuse import fake_use

from pypitools import common

SECTION = "pypitools"

    
def upload_by_setup(config: configparser.ConfigParser) -> None:
    fake_use(config)
    common.check_call_no_output([
        'python',
        'setup.py',
        'sdist',
        'upload',
        '-r',
        'pypi',
    ])


def upload_by_twine(config: configparser.ConfigParser) -> None:
    fake_use(config)
    common.check_call_no_output([
        'python3',
        'setup.py',
        'sdist',
    ])
    # at this point there should be only one file in the 'dist' folder
    file_list = list(os.listdir('dist'))
    assert len(file_list) == 1
    filename = file_list[0]
    full_filename = os.path.join('dist', filename)
    common.check_call_no_output([
        'twine',
        'upload',
        full_filename,
        # '--config-file',
        # common.config_file,
    ])


def upload_by_gemfury(config: configparser.ConfigParser) -> None:
    p_gemfury_user = config.get(SECTION, "gemfury_user")
    common.check_call_no_output([
        'python3',
        'setup.py',
        'sdist',
    ])
    # at this point there should be only one file in the 'dist' folder
    file_list = list(os.listdir('dist'))
    assert len(file_list) == 1
    filename = file_list[0]
    full_filename = os.path.join('dist', filename)
    common.check_call_no_output([
        'fury',
        'push',
        '--as={}'.format(p_gemfury_user),
        full_filename,
    ])


@click.command()
def main():
    common.setup_main()
    # read setup.cfg config file
    config = configparser.ConfigParser()
    config.read("setup.cfg")
    p_method = config.get(SECTION, "method")
    assert p_method in ["setup", "twine", "gemfury"]
    p_clean_before = config.getboolean(SECTION, "clean_before")
    p_clean_after = config.getboolean(SECTION, "clean_after")
    if p_clean_before:
        common.git_clean_full()
    try:
        if p_method == "setup":
            upload_by_setup(config)
        if p_method == "twine":
            upload_by_twine(config)
        if p_method == "gemfury":
            upload_by_gemfury(config)
    finally:
        if p_clean_after:
            common.git_clean_full()
