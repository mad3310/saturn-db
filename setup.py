#!/usr/bin/env python

from setuptools import setup, find_packages

install_description = '''
saturn db
===========

Python library for Saturn Database
'''

setup(
    name='saturn-db',
    version='0.0.1',
    license='SATURN',
    description='Python library for saturn DB System',
    long_description=install_description,
    author='chenwenquan',
    author_email='wqchenxjtu@163.com',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'python-envcfg>=0.1.0',
        'MySQL-python>=1.2.5',
        'requests>=2.3.0',
        'simplejson>=3.6.3',
        'dsnparse>=0.1.3',
    ],
    classifiers=['Private :: Do Not Upload'],
)
