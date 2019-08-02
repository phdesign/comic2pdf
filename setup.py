#!/usr/bin/env python3

"""
Python setuptools install script.

Usage:
$ python setup.py install               # install globally
$ python setup.py install --user        # install for user
$ python setup.py develop               # install symlink for development
$ python setup.py develop --uninstall   # uninstall for development
$ python setup.py sdist                 # create package in /dist
"""

from setuptools import setup

VERSION = "3.0.1"

with open("README.md") as f:
    readme = f.read()

setup(
    name="comic2pdf",
    version=VERSION,
    description="Converts .cbr and .cbz files to .pdf",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Paul Heasley",
    author_email="paul@phdesign.com.au",
    url="http://www.phdesign.com.au/comic2pdf",
    download_url=f"https://github.com/phdesign/comic2pdf/archive/v{VERSION}.tar.gz",
    scripts=["comic2pdf.py"],
    entry_points={"console_scripts": ["comic2pdf=comic2pdf:main"]},
    license="WTFPL",
    keywords=["comic", "pdf", "cbr", "cbz", "convert"],
    install_requires=["patool", "pillow"],
    zip_safe=True,
)
