from typing import List


console_scripts: List[str] = [
    "pypitools=pypitools.main:main",
]
config_requires: List[str] = []
dev_requires: List[str] = [
    "pypitools",
    "black",
]
install_requires: List[str] = [
    "pytconf",
    "pylogconf",
    "twine",
    "wheel",
]
make_requires: List[str] = [
    "pyclassifiers",
    "pydmt",
    "sphinx",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pymakehelper",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
