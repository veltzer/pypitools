from typing import List


console_scripts: List[str] = [
    "pypitools=pypitools.main:main",
]
dev_requires: List[str] = [
    "pypitools",
    "black",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "pytconf",
    "pylogconf",
    "twine",
    "wheel",
]
build_requires: List[str] = [
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pymakehelper",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
