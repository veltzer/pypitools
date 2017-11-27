<%!
    import config.python
    import config.personal
    import config.project
    import pypitools.version
%>import setuptools

# until we make printing pretty
# noinspection PyPep8
setuptools.setup(
    name='${config.project.project_name}',
    version='${pypitools.version.version_str}',
    description='${config.project.project_description}',
    long_description='${config.project.project_long_description}',
    author='${config.personal.personal_fullname}',
    author_email='${config.personal.personal_email}',
    maintainer='${config.personal.personal_fullname}',
    maintainer_email='${config.personal.personal_email}',
    keywords=${config.project.project_keywords},
    url='${config.project.project_website}',
    download_url='${config.project.project_website_download_src}',
    license='${config.project.project_license}',
    platforms=${config.project.project_platforms},
    packages=setuptools.find_packages(),
    classifiers=${config.project.project_classifiers},
    data_files=${config.project.project_data_files},
    python_requires="${config.python.python_requires}",
    install_requires=${config.python.install_requires},
    entry_points=${config.python.entry_points},
)
