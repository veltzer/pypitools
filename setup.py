import setuptools

import sys
if not sys.version_info[0] == 3:
    sys.exit("Sorry, only python version 3 is supported")

setuptools.setup(
    name='pypitools',
    version='0.0.1',
    description='pypitools is a collection of utilities to help interact with the pypi repository',
    long_description='pypitools helps you with various pypi tasks',
    url='https://veltzer.github.io/pypitools',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License'
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='pypi register upload erase delete',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'pypi_install_from_local=pypitools.install_from_local:main',
            'pypi_install_from_pypi=pypitools.install_from_pypi:main',
            'pypi_register=pypitools.register:main',
            'pypi_upload=pypitools.upload:main',
        ],
    },
)
