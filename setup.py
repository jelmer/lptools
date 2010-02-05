#!/usr/bin/python

from glob import glob
from distutils.core import setup

setup(
    name='lptools',
    version='0.1',
    url='https://launchpad.net/lptools',
    author='Rodney Dawes',
    author_email='rodney.dawes@canonical.com',
    license='GPLv3',
    description='A collection of tools for developers who use launchpad',
    py_modules=[],
    scripts=glob('bin/*'),
    )

