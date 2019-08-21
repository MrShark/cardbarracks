# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

setup(
    name='cardbarracks',
    version='0.1',
    description='Tools to generate statuscards for wargaming miniatures',
    long_description=readme,
    author='Jens Persson',
    author_email='jens@persson.cx',
    url='https://localhost/',
    license=license,
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'cardbarracks=cardbarracks.commandline:script',
        ],
    },
)
