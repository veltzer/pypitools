console_scripts = [
    "pypitools=pypitools.main:main",
]
dev_requires = [
    "pypitools",
    "black",
]
make_requires = [
    "pyclassifiers",
    "pydmt",
    "Sphinx",
]
install_requires = [
    "pytconf",
    "pylogconf",
    "twine",
    "wheel",
]
test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pymakehelper",
    "mypy",
]
