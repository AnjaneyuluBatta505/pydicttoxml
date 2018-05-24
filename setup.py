# -*- coding: utf-8 -*-
import os
import sys
from distutils.core import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("This version of Pydicttoxml requires Python {}.{},\
        but you're trying to install it on Python {}.{}.".format(
        *(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)
setup(
    name='pydicttoxml',
    version='1.0.1',
    description='Convert python dictionary into a xml equivalent format',
    author=u'Anjaneyulu Batta',
    author_email='anjaneyulu.batta505@gmail.com',
    url='https://github.com/AnjaneyuluBatta505/pydicttoxml',
    packages=['pydicttoxml'],
    keywords="convert dictionary into a xml",
    long_description=read('README.rst'),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: XML'
    ],
    license='MIT'
)
