import setuptools

import sys
if not sys.version_info[0] == 3:
    sys.exit("Sorry, only python version 3 is supported")

setuptools.setup(
    name='pypitools',
    version='0.0.19',
    description='pypitools is a collection of utilities to help interact with the pypi repository',
    long_description='pypitools helps you with various pypi tasks',
    url='https://veltzer.github.io/pypitools',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='pypi register upload erase delete',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    install_requires=[
        'click',  # for command line parsing
        'pyfakeuse'  # for fake use of variables
    ],
    entry_points={
        'console_scripts': [
            'pypitools_install_from_local=pypitools.scripts.install_from_local:main',
            'pypitools_install_from_remote=pypitools.scripts.install_from_remote:main',
            'pypitools_register=pypitools.scripts.register:main',
            'pypitools_upload=pypitools.scripts.upload:main',
            'pypitools_check_config=pypitools.scripts.check_config:main',
        ],
    },
)
