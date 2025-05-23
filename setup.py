import setuptools


def get_readme():
    with open("README.rst") as f:
        return f.read()


setuptools.setup(
    # the first three fields are a must according to the documentation
    name="pypitools",
    version="0.0.79",
    packages=[
        "pypitools",
    ],
    # from here all is optional
    description="pypitools helps you with various pypi tasks",
    long_description=get_readme(),
    long_description_content_type="text/x-rst",
    author="Mark Veltzer",
    author_email="mark.veltzer@gmail.com",
    maintainer="Mark Veltzer",
    maintainer_email="mark.veltzer@gmail.com",
    keywords=[
        "pypi",
        "register",
        "upload",
        "erase",
        "delete",
    ],
    url="https://veltzer.github.io/pypitools",
    download_url="https://github.com/veltzer/pypitools",
    license="MIT",
    platforms=[
        "python3",
    ],
    install_requires=[
        "pytconf",
        "pylogconf",
        "twine",
        "wheel",
        "setuptools",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": [
        "pypitools=pypitools.main:main",
    ]},
)
