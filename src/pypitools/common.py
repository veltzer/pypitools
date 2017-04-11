import subprocess
import os.path

import sys
from pyfakeuse.pyfakeuse import fake_use


def get_config_file():
    return os.path.expanduser('~/.pypirc')


def check_call_no_output(args):
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


def git_clean_full():
    check_call_no_output([
        'git',
        'clean',
        '-qffxd',
    ])


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
