# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
__VERSION__ = '0.9.0'

setup(
    name='cryptsy_api',
    version=__VERSION__,
    description="Python library for all cryptsy.com API's.",
    long_description=(open('README.rst').read()),
    author='Mathias Seidler',
    author_email='seishin@gmail.com',
    maintainer='Mathias Seidler',
    maintainer_email='seishin@gmail.com',
    url='http://github.com/katakumpo/cryptsy_api',
    license='MIT License',
    platforms=['any'],
    packages=find_packages(exclude=['tests*', '.tox*']),
    install_requires=[],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Education :: Testing',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: General',
        'Topic :: Utilities',
    ],
)
