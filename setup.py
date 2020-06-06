import setuptools

setuptools.setup(
    # the first three fields are a must according to the documentation
    name="pypitools",
    version="0.0.57",
    packages=[
        'pypitools',
        'pypitools.endpoints',
    ],
    # from here all is optional
    description="pypitools helps you with various pypi tasks",
    long_description="pypitools is a collection of utilities to help interact with the pypi repository",
    long_description_content_type="text/x-rst",
    author="Mark Veltzer",
    author_email="mark.veltzer@gmail.com",
    maintainer="Mark Veltzer",
    maintainer_email="mark.veltzer@gmail.com",
    keywords=[
        'pypi',
        'register',
        'upload',
        'erase',
        'delete',
    ],
    url="https://veltzer.github.io/pypitools",
    download_url="https://github.com/veltzer/pypitools",
    license="MIT",
    platforms=[
        'python3',
    ],
    install_requires=[
        'pytconf',
        'pylogconf',
        'twine',
        'wheel',
    ],
    extras_require={
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
    data_files=[
    ],
    entry_points={"console_scripts": [
        'pypitools=pypitools.endpoints.main:main',
    ]},
    python_requires=">=3.5",
)
