"""
This is common pypitools functionality
"""

import subprocess
import os
import logging

from pypitools.configs import ConfigData, UploadMethod, RegisterMethod


def check_call_no_output(args) -> None:
    """
    Run a process and check that it returns an OK return code
    and has no output
    :param args:
    """
    logger = logging.getLogger(__name__)
    logger.debug("running %s", args)
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
    (res_stdout, res_stderr) = process.communicate()
    if process.returncode:
        print(res_stdout, end="")
        print(res_stderr, end="")
        raise ValueError(
            "exit code from [{}] was [{}]".format(" ".join(args), process.returncode)
        )


def git_clean_full() -> None:
    """
    Clean the current git repo in a strict way
    """
    check_call_no_output(["git", "clean", "-qffxd"])


def get_package_fullname() -> str:
    """
    Get the full name of the package
    """
    output = subprocess.check_output(
        ["{}".format(ConfigData.python), "setup.py", "--fullname"]
    ).decode()
    return output.rstrip()


def get_package_filename() -> str:
    """
    Get the package filename
    """
    return os.path.join("dist", get_package_fullname() + ".tar.gz")


def get_package_wheelname() -> str:
    """
    Get the package wheelname
    """
    return os.path.join("dist", get_package_fullname() + "-py3-none-any.whl")


def upload_by_setup() -> None:
    """
    upload by setup.py sdist upload

    This method still works although it is legacy
    
    see: python setup.py upload --help
    """
    args = [
        "{}".format(ConfigData.python),
        "setup.py",
    ]
    if ConfigData.upload_sdist:
        args.append("sdist")
    if ConfigData.upload_wheel:
        args.append("bdist_wheel")
    args.extend(
        [
            "upload",
            # this means which repository to upload too
            # the default is https://upload.pypi.org/legacy/ and it works
            # '-r',
            # 'pypi',
        ]
    )
    check_call_no_output(args)


def upload_by_twine() -> None:
    """
    upload by twine
    """
    package_it()
    args = [
        "twine",
        "upload",
    ]
    if ConfigData.upload_sdist:
        args.append(get_package_filename())
    if ConfigData.upload_wheel:
        args.append(get_package_wheelname())
    check_call_no_output(args)


def check_by_twine() -> None:
    """
    check by twine
    """
    args = [
        "twine",
        "check",
    ]
    if ConfigData.upload_sdist:
        args.append(get_package_filename())
    if ConfigData.upload_wheel:
        args.append(get_package_wheelname())
    check_call_no_output(args)


def upload_by_gemfury() -> None:
    """
    upload to gemfury
    """
    package_it()
    # The command line is the one recommended by gemfury at
    # https://manage.fury.io/dashboard/[username]/push
    check_call_no_output(
        [
            "fury",
            "push",
            get_package_filename(),
            "--as={}".format(ConfigData.gemfury_user),
        ]
    )


def upload_select() -> None:
    """
    upload via the method configured
    """
    if ConfigData.upload_method == UploadMethod.SETUP:
        upload_by_setup()
    if ConfigData.upload_method == UploadMethod.TWINE:
        upload_by_twine()
    if ConfigData.upload_method == UploadMethod.GEMFURY:
        upload_by_gemfury()


def register_select() -> None:
    """
    Register via the method configured
    """
    if ConfigData.register_method == RegisterMethod.TWINE:
        register_by_twine()
    if ConfigData.register_method == RegisterMethod.SETUP:
        register_by_setup()
    if ConfigData.register_method == RegisterMethod.UPLOAD:
        upload_select()


def register_by_setup() -> None:
    """
    register via setup.py register
    """
    check_call_no_output(
        ["{}".format(ConfigData.python), "setup.py", "register", "-r", "pypi"]
    )


def register_by_twine() -> None:
    """
    register via the twine method
    """
    package_it()
    check_call_no_output(["twine", "register", get_package_filename()])


def clean_before_if_needed() -> None:
    """
    Clean the git repo if needed
    """
    if ConfigData.clean_before:
        git_clean_full()


def clean_after_if_needed() -> None:
    """
    Clean the git repo if needed
    """
    if ConfigData.clean_after:
        git_clean_full()


def package_it() -> None:
    """
    package our module
    """
    args = [
        "{}".format(ConfigData.python),
        "setup.py",
    ]
    if ConfigData.upload_sdist:
        args.append("sdist")
    if ConfigData.upload_wheel:
        args.append("bdist_wheel")
    check_call_no_output(args)
