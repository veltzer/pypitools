import configparser
import subprocess
import os.path

import sys
from pyfakeuse.pyfakeuse import fake_use


def get_config_file() -> str:
    return os.path.expanduser('~/.pypirc')


def check_call_no_output(args) -> None:
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
        self.method = None
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
    config.read("setup.cfg")
    cfg = ConfigData()
    cfg.method = config.get(SECTION, "method")
    assert cfg.method in ["setup", "twine", "gemfury"]
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
    assert cfg.register_method in ["setup", "twine"]
    return cfg


def excepthook(exception_type, value, traceback):
    fake_use(exception_type)
    fake_use(traceback)
    # this loop will drill to the core of the problem
    # use only if this is what you want to show...
    while value.__cause__:
        value = value.__cause__
    print(value)


def setup_main():
    sys.excepthook = excepthook
