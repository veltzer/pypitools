import configparser
import subprocess
import os.path
import logging

import sys
from pyfakeuse.pyfakeuse import fake_use


logger = logging.getLogger(__name__)


def get_config_file() -> str:
    return os.path.expanduser('~/.pypirc')


def check_call_no_output(args) -> None:
    logger.debug("running %s", args)
    p = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    (res_stdout, res_stderr) = p.communicate()
    if p.returncode:
        res_stdout = res_stdout.decode()
        res_stderr = res_stderr.decode()
        print(res_stdout, end='')
        print(res_stderr, end='')
        raise ValueError('exit code from [{}] was [{}]'.format(" ".join(args), p.returncode))


def git_clean_full() -> None:
    check_call_no_output([
        'git',
        'clean',
        '-qffxd',
    ])


class ConfigData:
    def __init__(self):
        self.upload_method = None
        self.clean_before = None
        self.clean_after = None
        self.install_in_user_folder = None
        self.use_sudo = None
        self.pip_quiet = None
        self.setup_quiet = None
        self.pip = None
        self.gemfury_user = None
        self.python = None
        self.register_method = None


def read_config() -> ConfigData:
    SECTION = "pypitools"
    # read setup.cfg config file
    config = configparser.ConfigParser()
    homedir_filename = os.path.expanduser("~/.setup.cfg")
    if os.path.isfile(homedir_filename):
        config.read(homedir_filename)
    local_filename = "setup.cfg"
    if os.path.isfile(local_filename):
        config.read(local_filename)
    cfg = ConfigData()
    cfg.upload_method = config.get(SECTION, "upload_method")
    assert cfg.upload_method in ["setup", "twine", "gemfury"]
    cfg.clean_before = config.getboolean(SECTION, "clean_before")
    cfg.clean_after = config.getboolean(SECTION, "clean_after")
    cfg.install_in_user_folder = config.getboolean(SECTION, "install_in_user_folder")
    cfg.use_sudo = config.getboolean(SECTION, "use_sudo")
    cfg.pip_quiet = config.getboolean(SECTION, "pip_quiet")
    cfg.setup_quiet = config.getboolean(SECTION, "setup_quiet")
    cfg.pip = config.get(SECTION, "pip")
    cfg.gemfury_user = config.get(SECTION, "gemfury_user")
    cfg.python = config.get(SECTION, "python")
    cfg.register_method = config.get(SECTION, "register_method")
    assert cfg.register_method in ["setup", "twine", "upload"]
    return cfg


def excepthook(exception_type, value, traceback) -> None:
    fake_use(exception_type)
    fake_use(traceback)
    # this loop will drill to the core of the problem
    # use only if this is what you want to show...
    while value.__cause__:
        value = value.__cause__
    print(value)


def setup_main() -> None:
    sys.excepthook = excepthook


def get_package_version(config: ConfigData) -> str:
    output = subprocess.check_output([
        '{}'.format(config.python),
        'setup.py',
        '--version',
    ]).decode()
    return output.rstrip()


def get_package_fullname(config: ConfigData) -> str:
    output = subprocess.check_output([
        '{}'.format(config.python),
        'setup.py',
        '--fullname',
    ]).decode()
    return output.rstrip()


def get_package_filename(config: ConfigData) -> str:
    return os.path.join("dist", get_package_fullname(config)+".tar.gz")


def upload_by_setup(config: ConfigData) -> None:
    check_call_no_output([
        '{}'.format(config.python),
        'setup.py',
        'sdist',
        'upload',
        '-r',
        'pypi',
    ])


def upload_by_twine(config: ConfigData) -> None:
    check_call_no_output([
        '{}'.format(config.python),
        'setup.py',
        'sdist',
    ])
    filename = get_package_filename(config)
    check_call_no_output([
        'twine',
        'upload',
        filename,
        # '--config-file',
        # common.config_file,
    ])


def upload_by_gemfury(config: ConfigData) -> None:
    check_call_no_output([
        '{}'.format(config.python),
        'setup.py',
        'sdist',
    ])
    filename = get_package_filename(config)
    check_call_no_output([
        'fury',
        'push',
        '--as={}'.format(config.gemfury_user),
        filename,
    ])


def upload(config: ConfigData) -> None:
    if config.upload_method == "setup":
        upload_by_setup(config)
    if config.upload_method == "twine":
        upload_by_twine(config)
    if config.upload_method == "gemfury":
        upload_by_gemfury(config)
