import setuptools

# until we make printing pretty
# noinspection PyPep8
setuptools.setup(
    name='pypitools',
    version='0.0.38',
    description='pypitools helps you with various pypi tasks',
    long_description='pypitools is a collection of utilities to help interact with the pypi repository',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    maintainer='Mark Veltzer',
    maintainer_email='mark.veltzer@gmail.com',
    keywords=['pypi', 'register', 'upload', 'erase', 'delete'],
    url='https://veltzer.github.io/pypitools',
    download_url='https://github.com/veltzer/pypitools',
    license='MIT',
    platforms=['python3'],
    packages=setuptools.find_packages(),
    install_requires=['click', 'pylogconf'],
    classifiers=['Development Status :: 4 - Beta', 'Environment :: Console', 'Operating System :: OS Independent', 'Programming Language :: Python', 'Programming Language :: Python :: 3', 'Topic :: Utilities'],
    data_files=[],
    entry_points={'console_scripts': ['pypitools_install_from_local=pypitools.scripts.install_from_local:main', 'pypitools_install_from_remote=pypitools.scripts.install_from_remote:main', 'pypitools_register=pypitools.scripts.register:main', 'pypitools_upload=pypitools.scripts.upload:main', 'pypitools_check_config=pypitools.scripts.check_config:main']},
)
