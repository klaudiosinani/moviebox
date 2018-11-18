# -*- coding: utf-8 -*-
import moviebox

from setuptools import setup
from os.path import join, dirname

movieboxVersion = moviebox.__version__
longDescription = open(join(dirname(__file__), 'readme.md')).read()

setup(
    name='moviebox',
    version=movieboxVersion,
    url='https://github.com/klaussinani/moviebox',
    license='MIT',
    author='Klaus Sinani',
    author_email='klaussinani@gmail.com',
    description='Machine learning movie recommender',
    long_description=longDescription,
    include_package_data=True,
    packages=['moviebox'],
    classifiers=[
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=2.7.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    install_requires=[
        'click', 'pandas', 'scikit-learn', 'termcolor', 'colorama'
    ],
    entry_points={
        'console_scripts': ['moviebox=moviebox.cli:main'],
    })
