#!/usr/bin/env python
# -*- coding: utf-8 -*-

# modify from https://github.com/kennethreitz/setup.py/blob/master/setup.py

import io
import os
import importlib.util

from setuptools import find_packages, setup

def red_warn(warning_text:str):
    print(f'\033[31m{warning_text}\033[0m')
    print()

def get_version(project_name: str):
    spec = importlib.util.find_spec(project_name)
    if spec is not None:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, '__version__'):
            return module.__version__
        else:
            red_warn(f"Module {project_name} does not have attribute '__version__'.")
    else:
        raise ImportError(f"Module {project_name} not found.")

here = os.path.abspath(os.path.dirname(__file__))

# ----------------------- Basic Info -----------------------
NAME = 'your_package_name' # should be the same as the folder name <package-name>
VERSION = get_version(NAME)

AUTHOR = 'your_name'
EMAIL = 'your_email@email.com'

URL = 'https://github.com/YOUR/REPO'
DESCRIPTION = 'your_package_description'

# Import the README and use it as the long-description.
# Note: please upgrade `setuptools` using `pip install -U setuptools`, 
# or bellow code will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), 'r' , encoding='utf-8') as ldf: # long description file
        LONG_DESCRIPTION = '\n' + ldf.read()
except FileNotFoundError:
    red_warn(f'README.md not found in {here}, use below as LONG_DESCRIPTION!')
    LONG_DESCRIPTION = DESCRIPTION

# Find License file, and import it as LICENSE variable.
# Note: please upgrade `setuptools` using `pip install -U setuptools`, 
# or bellow code will only work if the license file is present in your MANIFEST.in file!   
license_file = [file for file in os.listdir(here) if 'license' in file.lower()]
try:
    with io.open(os.path.join(here, license_file[-1]), 'r', encoding='utf-8') as lf: # license file
        LICENSE = '\n' + lf.read()
except FileNotFoundError:
    red_warn(f'License file not found in {here}, use MIT as default license!')
    LICENSE = "MIT"

# ----------------------- Requirement Info -----------------------
REQUIRES_PYTHON = '>=3.6.0'
ONLY_PACKAGE = True # will be parse to `include_package_data` in setup() 

# Load requirements.txt content to be REQUIRED variable.
# Note: this will only work if 'requirements.txt' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'requirements.txt'), 'r', encoding='utf-8') as rf: # requirements file
        REQUIRED = [l.strip() for l in rf.readlines()]
except FileNotFoundError:
    red_warn(f'requirements.txt not found in {here}, third-party packages should be downloaded manmally!')
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
                                  "tests.*",
                                  "docs", "doc", "document", "documents", 
                                  "example", "examples"])

# ----------------------- Other Info -----------------------
# build cli tool, enable `entry_points` in setup()

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
    include_package_data=ONLY_PACKAGE, # only files inside the package directory are included in the final wheel
    
    classifiers=TAGS,
    packages=PACKAGES,
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={ # command line interface
    #     'command': ['my_package.module:function'], # command=my_package.module:function
    # }
)