import os
import subprocess

import click

import pypitools.common
from pypitools import common


@click.command()
@click.option('--debug', required=False, default=False, type=bool, help="debug the app")
def main(debug: bool):
    common.setup_main(debug)
    config = common.read_config()
    module_name = os.path.basename(os.getcwd())
    args = []
    if config.use_sudo:
        args.extend([
            'sudo',
            '-H',
        ])
    args.extend([
        '{}'.format(config.pip),
        'install',
        '--upgrade',
        '{module_name}'.format(module_name=module_name),
    ])
    if config.pip_quiet:
        args.extend([
            '--quiet',
        ])
    if config.install_in_user_folder:
        args.extend([
            '--user',
        ])
    pypitools.common.check_call_no_output(args)
    output = subprocess.check_output([
        '{}'.format(config.pip),
        'show',
        '{module_name}'.format(module_name=module_name),
    ]).decode()
    for line in output.split("\n"):
        if line.startswith("Version"):
            print(line)
