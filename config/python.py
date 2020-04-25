import config.project

package_name = config.project.project_name

console_scripts = [
    'pypitools=pypitools.endpoints.main:main',
]

setup_requires = [
]

run_requires = [
    'pytconf',  # for command line parsing
    'pylogconf',  # for configuring logging
    'twine',  # for doing some of the work
]

test_requires = [
    'pylint',  # to check for lint errors
    'pytest',  # for testing
    'pyflakes',  # for testing
]

dev_requires = [
    'pyclassifiers',  # for software classification
    'pypitools',  # for upload etc
    'pydmt',  # for building
    'Sphinx',  # for the sphinx builder
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3"
