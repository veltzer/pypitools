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
import click

from pypitools import common
from pypitools.common import ConfigData


def register_by_setup(config: ConfigData) -> None:
    common.check_call_no_output([
        '{}'.format(config.python),
        'setup.py',
        'register',
        '-r',
        'pypi',
    ])


def register_by_twine(config: ConfigData) -> None:
    common.check_call_no_output([
        '{}'.format(config.python),
        'setup.py',
        'bdist_wheel',
    ])

    # at this point there should be only one file in the 'dist' folder
    filename = common.get_package_filename(config)
    common.check_call_no_output([
        'twine',
        'register',
        filename,
    ])


@click.command()
@click.option(
    '--debug',
    required=False,
    default=False,
    type=bool,
    help="debug the app",
    show_defaults=True,
)
def main(debug: bool):
    common.setup_main(debug)
    config = common.read_config()
    if config.clean_before:
        common.git_clean_full()
    try:
        if config.register_method == "twine":
            register_by_twine(config)
        if config.register_method == "setup":
            register_by_setup(config)
        if config.register_method == "upload":
            common.upload(config)
    finally:
        if config.clean_after:
            common.git_clean_full()
