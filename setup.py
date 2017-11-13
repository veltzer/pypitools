import setuptools

setuptools.setup(
    name='pypitools',
    version='0.0.24',
    description='pypitools is a collection of utilities to help interact with the pypi repository',
    long_description='pypitools helps you with various pypi tasks',
    url='https://github.com/veltzer/pypitools',
    download_url='https://github.com/veltzer/pypitools',
    docs_url='https://veltzer.github.io/pypitools'
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    maintainer='Mark Veltzer',
    maintainer_email='mark.veltzer@gmail.com',
    license='MIT',
    platforms=['python3'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='pypi register upload erase delete',
    packages=setuptools.find_packages(),
    python_requires=">=3",
    install_requires=[
        'click',  # for command line parsing
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
