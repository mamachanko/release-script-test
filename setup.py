# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    description = f.read()


setup(
    name='release-script-test',
    version='0.18.0-dev',
    packages=find_packages(),
    namespace_packages=['dhh'],
    description=u'for testing release-script',
    long_description=description,
)
