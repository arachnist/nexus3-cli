# -*- coding: utf-8 -*-
import os
from io import open
from setuptools import find_packages, setup

package_name = 'nexus3-cli'
package_version = '0.1.0'

requires = [
    'docopt',
    'py',
    'future',
    'requests[security]>=2.14.2',
]

test_requires = [
    'flake8',
    'pytest-cov',
    'pytest-helpers-namespace',
    'pytest-mock',
    'pytest-faker',
]

with open('README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

setup(
    author='Thiago Figueiró',
    name=package_name,
    version=package_version,
    description='A python-based CLI for Sonatype Nexus OSS 3',
    long_description=readme,
    install_requires=requires,
    tests_require=test_requires,
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages('src'),
    # packages=['nexuscli'],
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'nexus3=nexuscli.cli:main',
        ],
    },
    extras_require={'test': test_requires},
)
