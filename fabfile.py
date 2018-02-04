# -*- coding: utf-8 -*-
from fabric.api import local, task


@task
def clean():
    # Clean-up compiled files
    local('python ./bin/clean.py && fclear python')


@task(alias='i')
def install():
    # Install dependencies
    local('pip install -r requirements.txt')


@task(default=True)
def test():
    # Check code for errors
    local('flake8 --show-source --count')


@task
def fix():
    # Automatically fix code errors with yapf
    local('yapf -ir .')


@task
def start():
    # Run the API
    local('python -m moviebox.main')


@task
def dist():

    # Build the source code
    local('python setup.py sdist bdist_wheel --universal')
