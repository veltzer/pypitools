"""
This script checks you config file
"""
import click

from pypitools import common


@click.command()
@click.option('--debug', required=False, default=False, type=bool, help="debug the app")
def main(debug: bool):
    common.setup_main(debug)
    common.read_config()
