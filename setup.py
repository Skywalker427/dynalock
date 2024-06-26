#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "boto3>=1.34.74",
    "botocore>=1.34.74",
]

test_requirements = ['pytest>=3', ]

setup(
    author="Hamzah Bawah",
    author_email='bhamza123@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Distributed locking with DynamoDB",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='dynalock',
    name='dynalock',
    packages=find_packages(include=['dynalock', 'dynalock.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/skywalker427/dynalock',
    version='0.3.0',
    zip_safe=False,
)
