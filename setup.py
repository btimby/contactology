#!/bin/env python

import os
from distutils.core import setup

name = 'contactology'
version = '0.1'
release = '1'
versrel = version + '-' + release
readme = os.path.join(os.path.dirname(__file__), 'README.rst')
long_description = file(readme).read()

setup(
    name = name,
    version = versrel,
    description = 'Contactology API client.',
    long_description = long_description,
    author = 'Contactology',
    author_email = 'info@contactology.com',
    maintainer = 'Ben Timby',
    maintainer_email = 'btimby@gmail.com',
    url = 'http://github.com/btimby/' + name + '/',
    license = 'MIT',
    requires = [],
    py_modules = [
        "contactology",
    ],
    classifiers = (
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
