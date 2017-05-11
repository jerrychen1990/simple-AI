#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/11/17 3:11 PM
# @Author  : xiaowa

from setuptools import setup, find_packages

import app

long_description = """ funny pretty simple AI games """

setup(
        name='simple-AI',
        version=app.__version__,
        description='funny pretty simple AI games ',
        long_description=long_description,
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Topic :: Documentation",
        ],
        keywords='simple-AI',
        author='jerrychen',
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'guess-num = app.commands:guess_num_commandline',
            ]
        },
        install_requires=[
        ]
)
