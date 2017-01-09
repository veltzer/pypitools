import os
import subprocess
import pypitools.common


def main():
    # PIP="pip"
    PIP = "pip3"
    module = os.path.basename(os.getcwd())
    pypitools.common.check_call_no_output([
        "sudo",
        "-H",
        "{PIP}".format(PIP=PIP),
        "install",
        "--quiet",
        "--upgrade",
        "{module}".format(module=module),
    ])
    output = subprocess.check_output([
        "{PIP}".format(PIP=PIP),
        "show",
        "{module}".format(module=module),
    ]).decode()
    for line in output.split("\n"):
        if line.startswith("Version"):
            print(line)
