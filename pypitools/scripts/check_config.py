import click

from pypitools import common


@click.command()
@click.option(
    '--debug',
    required=False,
    default=False,
    type=bool,
    help="debug the app",
    show_default=True,
)
def main(debug: bool):
    """
    This script checks your config file
    """
    common.setup_main(debug)
    common.read_config()


if __name__ == '__main__':
    main()
