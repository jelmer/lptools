#!/usr/bin/python3

from glob import glob
from distutils.core import setup
import os.path

with open(os.path.join(os.path.dirname(__file__), 'README'), 'r') as f:
    description = f.read()

setup(
    name='lptools',
    version='0.2.0',
    url='https://launchpad.net/lptools',
    author='Rodney Dawes',
    author_email='rodney.dawes@canonical.com',
    license='GPLv3',
    description='A collection of tools for developers who use launchpad',
    long_description=description,
    py_modules=[],
    data_files=[('share/lptools/templates', ['templates/recipe-status.css',
                                             'templates/recipe-status.html'])],
    packages=['lptools'],
    scripts=glob('bin/*'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPL3)'
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        ],
    )

