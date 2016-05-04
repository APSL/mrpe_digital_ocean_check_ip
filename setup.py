
#!/usr/bin/env python

from __future__ import with_statement

import sys

from setuptools import setup, find_packages


setup(
    name='DigitalOceanCheckIP',
    version='0.1',
    description='Command to know if Digital ocean is assigned properly.',
    #long_description='',
    author='Edu Herraiz',
    author_email='eherraiz@apsl.net',
    url='https://www.apsl.net',
    packages=find_packages(),
    install_requires=[
        "requests",
        ],
    entry_points={
        'console_scripts': [
            'digital_ocean_check_ip = check.check:check',
        ]
    },
)
