"""
This script checks you config file
"""
import click

from pypitools import common


@click.command()
def main():
    common.setup_main()
    common.read_config()
