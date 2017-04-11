import os
import subprocess
import pypitools.common
from pypitools import common


def main():
    common.setup_main()
    # PIP="pip"
    pip = "pip3"
    module_name = os.path.basename(os.getcwd())
    pypitools.common.check_call_no_output([
        "sudo",
        "-H",
        "{pip}".format(pip=pip),
        "install",
        "--quiet",
        "--upgrade",
        "{module_name}".format(module_name=module_name),
    ])
    output = subprocess.check_output([
        "{pip}".format(pip=pip),
        "show",
        "{module_name}".format(module_name=module_name),
    ]).decode()
    for line in output.split("\n"):
        if line.startswith("Version"):
            print(line)
