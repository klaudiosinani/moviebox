import sys

from fabric.colors import red
from fabric.api import local, task


@task(default=True)
def check():
    # Get python version
    PY3 = sys.version_info[0] == 3
    # Python 3 check
    if not (PY3):
        print(red('Please install Python 3 to build the project.'))
        quit()


@task
def clean():
    # Clean-up compiled files
    local('./bin/clean.py && fclear python')


@task(alias='i')
def install():
    check()
    # Install dependencies
    local('pip3 install -r requirements.txt')


@task
def test():
    check()
    # Check code for errors
    local('flake8 --show-source --count')


@task
def fix():
    check()
    # Automatically fix code errors with yapf
    local('yapf -ir .')


@task
def start():
    check()
    # Run the API
    local('python3 -m moviebox.main')


@task
def dist():
    check()
    # Build the source code
    local('python3 setup.py sdist bdist_wheel')
