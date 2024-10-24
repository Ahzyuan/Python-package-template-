## 📦 A Project template for self-developed Python package

![Static Badge](https://img.shields.io/badge/Version-v1.0.1-green)
![Static Badge](https://img.shields.io/badge/Build-setuptools-red?link=https%3A%2F%2Fgithub.com%2Fpypa%2Fsetuptools)
![Static Badge](https://img.shields.io/badge/PyPi-Package_pattern-yellow?logo=pypi&labelColor=%23FAFAFA)

> Note:   
> - This repo is inspired by https://github.com/navdeep-G/setup.py, aiming to boot up your develop speed when you are creating a new Python package.  
> - This repo has been modified in strict accordance with the requirements of origin repo's license, and still adhere to the principle of open source sharing.

This repo exists to provide a project structure template, that can be used to accelerate the development of a Python third-party package.

## 🎯 Features

- A relatively complete project structure that complies with software engineering specifications, including functional directories: [code](package-name), [test](tests), [document](docs), and [project demonstration](examples)

- A fully configured [`setup.py`](setup.py). You don't need to look up the documents for the meaning of each package's metadata, comments are provided for most of them. Meanwhile, it allows dynamic matching of update information when building packages, including `version`, `README`, and project dependencies .

## 🔨 Getting Started

```bash
# <project-root> stand for anywhere you want to store your project
cd <project-root> 

# Note: specify the project name you want to use
git clone https://github.com/Ahzyuan/Python-package-template.git <your-project-name>

# replace <your-project-repo-url> with your repo url
cd <your-project-name>
git remote set-url origin <your-project-repo-url>
git pull 

# modify License, remember to specify your name below
# default license is MIT
sed -i "3s/<COPYRIGHT HOLDER>/your-name/" LICENSE
sed -i "3s/<YEAR>/$(date +%Y)/" LICENSE
```
after that, you should still configure the following files:
1. `setup.py`: modify the variables in upper case, such as `NAME`, `AUTHOR`, `EMAIL`, `DESCRIPTION`...
2. `requirements.txt`: add your dependencies
3. `MANIFEST.in`: configure which files should be included in the package
4. `package-name/__version__.py`: specify the version of your package, **ensure this file exist!!!**

## 📑 To Do

- [ ] Add full pipeline of package development, from project preparation to maintaining.
- [ ] Add CI/CD support, such as GitHub Actions
- [ ] Add `pyproject.toml` support
- [ ] Add linter

## 👀 See More

- [What is setup.py?] on Stack Overflow
- [Official Python Packaging User Guide](https://packaging.python.org)
- [Setuptools User Guide](https://setuptools.pypa.io/en/latest/userguide/index.html)
- [The Hitchhiker's Guide to Packaging]
- [Cookiecutter template for a Python package]

# 🧾 License

This is free and unencumbered software released into the public domain, modified from https://github.com/navdeep-G/setup.py.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any means.