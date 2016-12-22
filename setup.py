#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'django-haystack>=2.5.1',
]

test_requirements = [
    'python-dateutil',
    'geopy==0.95.1',

    'nose',
    'mock',
    'coverage',
]

setup(
    name='haystack_elasticsearch',
    version='0.1.0',
    description="A set of backends for using Elasticsearch on Haystack.",
    long_description=readme + '\n\n' + history,
    author="Bruno Marques",
    author_email='bruno@cravefood.services',
    url='https://github.com/CraveFood/django-haystack-elasticsearch',
    packages=[
        'haystack_elasticsearch',
    ],
    package_dir={'haystack_elasticsearch':
                 'haystack_elasticsearch'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='haystack_elasticsearch',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
