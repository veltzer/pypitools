entry_points = {
    'console_scripts': [
        'pypitools_install_from_local=pypitools.scripts.install_from_local:main',
        'pypitools_install_from_remote=pypitools.scripts.install_from_remote:main',
        'pypitools_register=pypitools.scripts.register:main',
        'pypitools_upload=pypitools.scripts.upload:main',
        'pypitools_check_config=pypitools.scripts.check_config:main',
    ],
}
install_requires = [
    'click',  # for command line parsing
    'pylogconf',  # for configuring logging
]
dev_requires = [
    'pypitools',  # for upload etc
    'pydmt',  # for building
    'Sphinx',  # for the sphinx builder
]
python_requires = ">=3"