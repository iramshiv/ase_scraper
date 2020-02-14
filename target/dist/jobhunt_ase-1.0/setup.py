#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'jobhunt_ase',
        version = '1.0',
        description = 'Wb Scraper / Git project',
        long_description = 'Web Scraping.',
        author = '',
        author_email = '',
        license = '',
        url = 'https://github.com/iramshiv/jobhunt_ase',
        scripts = [],
        packages = [],
        namespace_packages = [],
        py_modules = [
            'job_parser',
            'duration_check',
            'job_scraper',
            'user_input',
            'higher_order',
            'anonymous_function',
            'url_session',
            'url_checker',
            'page_scraper'
        ],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '',
        obsoletes = [],
    )
