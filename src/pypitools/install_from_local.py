import shutil
import subprocess
import os


def main():
    dist_folder = 'dist'

    if os.path.isdir(dist_folder):
        shutil.rmtree(dist_folder)
    # TODO: check that there is no output
    subprocess.check_call([
        'python3',
        'setup.py',
        '--quiet',
        'sdist',
    ])
    files = list(os.listdir(dist_folder))
    # TODO: give out a good assetion message
    assert len(files) == 1
    new_file = os.path.join(dist_folder, files[0])
    # TODO: check that there is no output
    subprocess.check_call([
        'sudo',
        '-H',
        'pip3',
        'install',
        '--quiet',
        '--upgrade',
        new_file,
    ])
