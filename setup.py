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

from setuptools import setup, find_packages

VERSION = "3.0"

setup(
    name="comic2pdf",
    version=VERSION,
    description="Converts .cbr and .cbz files to .pdf",
    author="Paul Heasley",
    author_email="paul@phdesign.com.au",
    scripts=["comic2pdf.py"],
    entry_points={
        "console_scripts": ["comic2pdf=comic2pdf:main"]
    },
    license="WTFPL",
    install_requires=[
        "patool",
        "pillow"
    ],
    zip_safe=True,
)
