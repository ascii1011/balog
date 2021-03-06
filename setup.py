from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

import os

tests_require = [
    'nose',
    'nose-cov',
    'mock',
    'jsonschema',
]

sqs_requires = [
    'boto',
]

kafka_requires = [
    'kafka-python>=0.9,<1.0.0',
    'kazoo>=2.0,<2.1',
    'tabulate==0.7.3'
]

version = open(os.path.join('balog', 'version.txt'), 'rt').read().strip()


setup(
    name='balog',
    version=version,
    description='Balanced event logging schema and library',
    url='https://github.com/balanced/balog/',
    author='Balanced',
    author_email='dev@balancedpayments.com',
    packages=find_packages(),
    install_requires=[
        'jsonschema',
        'structlog',
        'pytz',
        'iso8601',
        'coid',
        'venusian',
        # Notice: the original package name is colander, we have a branch here
        # git+git@github.com:victorlin/colander.git@polymorphism#egg=colander
        # since we cannot add the git repo in install_requires, so I release
        # my branch as ba-colander. I know there is `dependency_links`,
        # however, it's not recommended by pip, for more information, you
        # can reference to
        # https://groups.google.com/forum/#!topic/pypa-dev/tJ6HHPQpyJ4
        'ba-colander==1.0b1',
    ],
    extras_require=dict(
        tests=tests_require,
        sqs=sqs_requires,
        kafka=kafka_requires,
    ),
    tests_require=tests_require,
    test_suite='nose.collector',
)
