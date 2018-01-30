#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO(titusfranz): put setup requirements (distutils extensions, etc.) here
    pip==8.1.2
    bumpversion==0.5.3
    wheel==0.29.0
    watchdog==0.8.3
    flake8==2.6.0
    tox==2.3.1
    coverage==4.1
    Sphinx==1.4.8
    cryptography==1.7
    PyYAML==3.11
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='wavelet_peak_detector',
    version='0.1.0',
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    long_description=readme + '\n\n' + history,
    author="Titus Franz",
    author_email='franzt@physi.uni-heidelberg.de',
    url='https://github.com/titusfranz/wavelet_peak_detector',
    packages=find_packages(include=['wavelet_peak_detector']),
    entry_points={
        'console_scripts': [
            'wavelet_peak_detector=wavelet_peak_detector.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='wavelet_peak_detector',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
