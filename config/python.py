import config.project

package_name = config.project.project_name

console_scripts = [
    'pypitools_install_from_local=pypitools.scripts.install_from_local:main',
    'pypitools_install_from_remote=pypitools.scripts.install_from_remote:main',
    'pypitools_register=pypitools.scripts.register:main',
    'pypitools_upload=pypitools.scripts.upload:main',
    'pypitools_check_config=pypitools.scripts.check_config:main',
]

setup_requires = [
]

run_requires = [
    'click',  # for command line parsing
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
