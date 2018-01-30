from setuptools import setup
from os.path import join, dirname

longDescription = open(join(dirname(__file__), 'readme.md')).read()

setup(
    name='moviebox',
    version='0.2.1',
    url='https://github.com/klauscfhq/moviebox',
    license='MIT',
    author='Klaus Sinani',
    author_email='klauscfhq@protonmail.com',
    description='Machine learning movie recommender',
    long_description=longDescription,
    include_package_data=True,
    packages=['moviebox'],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    install_requires=[
        'click', 'pandas', 'scikit-learn', 'termcolor', 'colorama'
    ],
    entry_points={
        'console_scripts': ['moviebox=moviebox.cli:main'],
    })
