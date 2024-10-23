## 📦 A Project template for self-developed Python package

> Note: This repo inspired by https://github.com/navdeep-G/setup.py, and has been modified in strict accordance with the requirements of its open source license, in order to get a better experience.

This repo exists to provide a project structure template, that can be used to guide you in developing third-party Python packages.

It has the following characteristics:

- A relatively complete software engineering project structure, including [code directory](package-name), [test directory](tests), [document directory](docs), and [demonstration directory](examples)

- `setup.py` is a collection of useful patterns and best practices. It extends the `python setup.py` command to achieve one-step code updates, package builds, and releases to [PyPi](https://pypi.org/) using `Twine`.

## 🔨Getting Started

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

- [ ] Add CI/CD support, such as GitHub Actions
- [ ] Add pyproject support

## 👀 See More

- [What is setup.py?] on Stack Overflow
- [Official Python Packaging User Guide](https://packaging.python.org)
- [The Hitchhiker's Guide to Packaging]
- [Cookiecutter template for a Python package]

# 🧾 License

This is free and unencumbered software released into the public domain, ,modified from https://github.com/navdeep-G/setup.py.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any means.

  [an example setup.py]: https://github.com/navdeep-G/setup.py/blob/master/setup.py
  [PyPi]: https://docs.python.org/3/distutils/packageindex.html
  [Twine]: https://pypi.python.org/pypi/twine
  [image]: https://farm1.staticflickr.com/628/33173824932_58add34581_k_d.jpg
  [What is setup.py?]: https://stackoverflow.com/questions/1471994/what-is-setup-py
  [The Hitchhiker's Guide to Packaging]: https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html
  [Cookiecutter template for a Python package]: https://github.com/audreyr/cookiecutter-pypackage
