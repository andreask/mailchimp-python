from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Mailchimp Python',
    version='0.1.12',
    description='A package used to integrate with Mailchimp via their public API (version 3)',
    long_description=long_description,
    url="https://github.com/andreask/mailchimp-python",
    author='Andréas Kühne',
    author_email='andreas@kuhne.se',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Communications',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mailchimp integration api',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'requests==2.24.0',
        'python-dateutil==2.8.1'
    ],
    test_suite="tests",
    tests_require=[
        'responses==0.10.15'
    ]
)
