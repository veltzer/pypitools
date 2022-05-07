import config.project

package_name = config.project.project_name

console_scripts = [
    "pypitools=pypitools.main:main",
]
dev_requires = [
    "pyclassifiers",
    "pypitools",
    "pydmt",
    "Sphinx",
    "black",
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
]

python_requires = ">=3.10"

test_os = ["ubuntu-22.04"]
test_python = ["3.10"]
