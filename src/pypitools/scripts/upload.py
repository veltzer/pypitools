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

import click

from pypitools import common


@click.command()
@click.option('--debug', required=False, default=True, type=bool, help="debug the app")
def main(debug: bool):
    common.setup_main(debug)
    config = common.read_config()
    if config.clean_before:
        common.git_clean_full()
    try:
        common.upload(config)
    finally:
        if config.clean_after:
            common.git_clean_full()
