#!/usr/bin/env python

from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='cb-response-surveyor',
    author='Keith McCammon',
    author_email='keith@redcanary.com',
    url='https://github.com/redcanaryco/redcanary-response-utils',
    license='MIT',
    packages=find_packages(),
    description='Tools to automate and/or expedite response.',
    version='0.1',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ],
    install_requires=[
        'cbapi'
        ]
    )
