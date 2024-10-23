#!/usr/bin/env python
# -*- coding: utf-8 -*-

# modify from https://github.com/kennethreitz/setup.py/blob/master/setup.py

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine[dev]

import re
import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

def get_version(project_name:str, version_file:str="__version__.py"):
    re_pattern = re.compile(r'(?<=[\'"])(.+)(?=[\'"])')
    
    project_name = project_name.lower().replace("-", "_").replace(" ", "_")
    
    version_file_path = os.path.join(sys.path[0], project_name, version_file)
    assert os.path.exists(version_file_path), f"Version file not found: {version_file_path}"
    
    version = ''
    with open(version_file_path,'r',encoding='utf-8') as f:
        for line in f.readlines():
            if line.startswith('__version__'):
                version = re.findall(re_pattern, line)[-1]
    
    assert len(version), f'Can not find version definition in {version_file_path}'
    return version

here = os.path.abspath(os.path.dirname(__file__))

def filenotfound_warn(warning_text:str):
    print(f'\033[31m{warning_text}\033[0m')
    print()

# ----------------------- Basic Info -----------------------
NAME = 'your_package_name'
VERSION = get_version(NAME, "__version__.py")

AUTHOR = 'your_name'
EMAIL = 'your_email@email.com'

URL = 'https://github.com/YOUR/REPO'
DESCRIPTION = 'your_package_description'

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), 'r' , encoding='utf-8') as ldf: # long description file
        LONG_DESCRIPTION = '\n' + ldf.read()
except FileNotFoundError:
    filenotfound_warn(f'README.md not found in {here}, use below as LONG_DESCRIPTION!')
    LONG_DESCRIPTION = DESCRIPTION

# Find License file, and import it as LICENSE variable.
# Note: this will only work if the license file is present in your MANIFEST.in file!   
license_file = [file for file in os.listdir(here) if 'license' in file.lower()]
try:
    with io.open(os.path.join(here, license_file[-1]), 'r', encoding='utf-8') as lf: # license file
        LICENSE = '\n' + lf.read()
except FileNotFoundError:
    filenotfound_warn(f'License file not found in {here}, use MIT as default license!')
    LICENSE = "MIT"

# ----------------------- Requirement Info -----------------------
REQUIRES_PYTHON = '>=3.6.0'

# Load requirements.txt content to be REQUIRED variable.
# Note: this will only work if 'requirements.txt' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'requirements.txt'), 'r', encoding='utf-8') as rf: # requirements file
        REQUIRED = [l.strip() for l in rf.readlines()]
except FileNotFoundError:
    filenotfound_warn(f'requirements.txt not found in {here}, third-party packages should be downloaded manmally!')
    REQUIRED = []

# Define packages use for test
TEST_REQUIRED = ['pytest', 'pytest-cov', 'tqdm', 'rich']

# Define optional packages
EXTRAS = {
    'docs': ['sphinx'],
    #'fancy feature': ['django'],
}

# ----------------------- Package structure Info -----------------------

TAGS = [
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]

PACKAGES = find_packages(exclude=["tests",  # Exclude these dir in building package even if there is a __init__.py in it
                                  "*.tests",
                                  "*.tests.*",
                                  "tests.*"])

# ----------------------- Other Info -----------------------
# build cli tool, enable `entry_points` in setup()

# enhance setup() function with self-defined command
class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(VERSION))
        os.system('git push --tags')

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    tests_requires=TEST_REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True if os.path.exists(os.path.join(here, 'MANIFEST.in')) else False,
    
    classifiers=TAGS,
    packages=PACKAGES,
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    entry_points={ # command line interface
        'touchgauge': ['touchgauge=touchgauge.cli:main'], # command=my_package.module:function
    },
    
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)