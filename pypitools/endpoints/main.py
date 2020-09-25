"""
main entry point to the program
"""
import os
import shutil
import subprocess

import pylogconf.core

from pypitools.configs import ConfigData
from pypitools.version import VERSION_STR
from pytconf import register_main, config_arg_parse_and_launch, register_endpoint

import pypitools
from pypitools.common import clean_before_if_needed, package_it, check_if_needed, upload_select,\
    clean_after_if_needed, \
    register_select, do_prerequisites
from pypitools.process_utils import check_call_collect


@register_endpoint()
def version() -> None:
    """
    print version
    """
    print(VERSION_STR)


@register_endpoint(
    configs=[ConfigData],
)
def install_from_local() -> None:
    """
    install a package from the local folder
    """
    dist_folder = "dist"

    if os.path.isdir(dist_folder):
        shutil.rmtree(dist_folder)
    args = [
        "{}".format(ConfigData.python),
        "setup.py",
        "sdist",
    ]
    if ConfigData.setup_quiet:
        args.extend(["--quiet"])
    check_call_collect(args)
    files = list(os.listdir(dist_folder))
    assert len(files) == 1, "too many files in {}".format(dist_folder)
    new_file = os.path.join(dist_folder, files[0])
    args = []
    if ConfigData.use_sudo:
        args.extend(["sudo", "-H"])
    args.extend(
        ["{}".format(ConfigData.pip), "install", "--quiet", "--upgrade", new_file]
    )
    if ConfigData.pip_quiet:
        args.extend(["--quiet"])
    if ConfigData.install_in_user_folder:
        args.extend(["--user"])
    check_call_collect(args)


@register_endpoint(
    configs=[ConfigData],
)
def install_from_remote() -> None:
    """
    install a package from pypi or gemfury
    """
    args = []
    if ConfigData.use_sudo:
        args.extend(["sudo", "-H"])
    args.extend(
        [
            "{}".format(ConfigData.pip),
            "install",
            "--upgrade",
            "{module_name}".format(module_name=ConfigData.module_name),
        ]
    )
    if ConfigData.pip_quiet:
        args.extend(["--quiet"])
    if ConfigData.install_in_user_folder:
        args.extend(["--user"])
    pypitools.process_utils.check_call_collect(args)
    output = subprocess.check_output(
        [
            "{}".format(ConfigData.pip),
            "show",
            "{module_name}".format(module_name=ConfigData.module_name),
        ]
    ).decode()
    for line in output.split("\n"):
        if line.startswith("Version"):
            print(line)


@register_endpoint(
    configs=[ConfigData],
)
def upload() -> None:
    """
    upload a package to pypi or gemfury

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
    clean_before_if_needed()
    package_it()
    check_if_needed()
    try:
        upload_select()
    finally:
        clean_after_if_needed()


@register_endpoint(
    configs=[ConfigData],
)
def register() -> None:
    """
    register a function on pypi or gemfury

    This function registers your project in pypi.

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
    clean_before_if_needed()
    package_it()
    check_if_needed()
    try:
        register_select()
    finally:
        clean_after_if_needed()


@register_endpoint(
    configs=[ConfigData],
)
def package() -> None:
    """
    package in source and/or wheel format
    """
    package_it()


@register_endpoint(
    configs=[ConfigData],
)
def check() -> None:
    """
    package and check if the package is correct
    """
    package_it()
    check_if_needed()


@register_endpoint(
    configs=[ConfigData],
)
def bump() -> None:
    """
    upgrade to new version

    This will:
    - check that all is committed
    - bump the version
    - run pydmt build
    - commit with a standard message
    - tag with a standard message
    - push
    - upload to pypi
    """
    # check_all_is_committed()
    check_if_needed()


@register_endpoint(
    configs=[ConfigData],
)
def prerequisites() -> None:
    """
    Get all pre requisites into a folder
    """
    do_prerequisites()


@register_endpoint(
    configs=[ConfigData],
)
def prerequisites_run() -> None:
    """
    Get run pre requisites into a folder
    """
    import config.python
    do_prerequisites(config.python.run_requires)


@register_main()
def main():
    """
    pypitools will help you interact with pypi
    """
    pylogconf.core.setup()
    config_arg_parse_and_launch()


if __name__ == "__main__":
    main()
