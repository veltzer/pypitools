"""
This is common pypitools functionality
"""

import subprocess
import os
import logging

from pypitools.configs import ConfigData, UploadMethod, RegisterMethod


def check_call_no_output(args):
    """
    Run a process and check that it returns an OK return code
    and has no output
    :param args:
    :return:
    """
    logger = logging.getLogger(__name__)
    logger.debug("running %s", args)
    process = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    (res_stdout, res_stderr) = process.communicate()
    if process.returncode:
        print(res_stdout, end='')
        print(res_stderr, end='')
        raise ValueError('exit code from [{}] was [{}]'.format(" ".join(args), process.returncode))


def git_clean_full():
    """
    Clean the current git repo in a strict way
    :return:
    """
    check_call_no_output([
        'git',
        'clean',
        '-qffxd',
    ])


def get_package_fullname():
    """
    Get the full name of the package
    :return:
    """
    output = subprocess.check_output([
        '{}'.format(ConfigData.python),
        'setup.py',
        '--fullname',
    ]).decode()
    return output.rstrip()


def get_package_filename():
    """
    Get the package filename
    :return:
    """
    return os.path.join("dist", get_package_fullname() + ".tar.gz")


def get_package_wheelname():
    """
    Get the package wheelname
    :return:
    """
    return os.path.join("dist", get_package_fullname() + "-py3-none-any.whl")


def upload_by_setup():
    """
    upload by setup.py sdist upload

    This method still works although it is legacy
    
    see: python setup.py upload --help
    :return:
    """
    args = [
        '{}'.format(ConfigData.python),
        'setup.py',
        'sdist',
    ]
    if ConfigData.wheel:
        args.append('bdist_wheel')
    args.extend([
        'upload',
        # this means which repository to upload too
        # the default is https://upload.pypi.org/legacy/ and it works
        # '-r',
        # 'pypi',
    ])
    check_call_no_output(args)


def upload_by_twine():
    """
    upload by twine
    :return:
    """
    package_it()
    args = [
        'twine',
        'upload',
        get_package_filename(),
    ]
    if ConfigData.wheel:
        args.append(get_package_wheelname())
    check_call_no_output(args)


def upload_by_gemfury():
    """
    upload to gemfury
    :return:
    """
    package_it()
    # The command line is the one recommended by gemfury at
    # https://manage.fury.io/dashboard/[username]/push
    check_call_no_output([
        'fury',
        'push',
        get_package_filename(),
        '--as={}'.format(ConfigData.gemfury_user),
    ])


def upload_select():
    """
    upload via the method configured
    :return:
    """
    if ConfigData.upload_method == UploadMethod.SETUP:
        upload_by_setup()
    if ConfigData.upload_method == UploadMethod.TWINE:
        upload_by_twine()
    if ConfigData.upload_method == UploadMethod.GEMFURY:
        upload_by_gemfury()


def register_select():
    """
    Register via the method configured
    :return:
    """
    if ConfigData.register_method == RegisterMethod.TWINE:
        register_by_twine()
    if ConfigData.register_method == RegisterMethod.SETUP:
        register_by_setup()
    if ConfigData.register_method == RegisterMethod.UPLOAD:
        upload_select()


def register_by_setup():
    """
    register via setup.py register
    :return:
    """
    check_call_no_output([
        '{}'.format(ConfigData.python),
        'setup.py',
        'register',
        '-r',
        'pypi',
    ])


def register_by_twine():
    """
    register via the twine method
    :return:
    """
    package_it()
    check_call_no_output([
        'twine',
        'register',
        get_package_filename(),
    ])


def clean_before_if_needed():
    """
    Clean the git repo if needed
    :return:
    """
    if ConfigData.clean_before:
        git_clean_full()


def clean_after_if_needed():
    """
    Clean the git repo if needed
    :return:
    """
    if ConfigData.clean_after:
        git_clean_full()


def package_it():
    args = [
        '{}'.format(ConfigData.python),
        'setup.py',
        'sdist',
    ]
    if ConfigData.wheel:
        args.append('bdist_wheel')
    check_call_no_output(args)
