import config.project

package_name = config.project.project_name

console_scripts = [
    "pypitools=pypitools.main:main",
]

setup_requires = []

run_requires = [
    "pytconf",  # for command line parsing
    "pylogconf",  # for configuring logging
    "twine",  # for doing some of the work
    "wheel",  # for packaging as wheel
]

test_requires = [
    "pylint",  # to check for lint errors
    "pytest",  # for testing
    "pytest-cov",  # for testing
    "flake8",  # for linting
    "pymakehelper",  # for make
]

dev_requires = [
    "pyclassifiers",  # for software classification
    "pypitools",  # for upload etc
    "pydmt",  # for building
    "Sphinx",  # for the sphinx builder
    "black",  # for source formatting
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.6"

extras_require = {
    # ':python_version == "2.7"': ['futures'],  # for python2.7 backport of concurrent.futures
}
