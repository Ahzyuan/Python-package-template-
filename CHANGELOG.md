
# v1.0.1

![](https://img.shields.io/badge/Version-v1.0.1-green)

## 🔄 Change

- Fix bugs in `setup.py`: Optimized the logic of dynamically obtaining version information, removed the extended function class `UploadCommand`(Cause `setpu.py` no longer supports functional customization, [see more](https://packaging.python.org/en/latest/discussions/setup-py-deprecated/#what-about-custom-commands))
- Fix bugs in `MANIFEST.in`: Discard unnecessary commands
- `<package-name>/__init__.py`: Added copyright definition and version definition
- `requirements.txt`: Added example dependencies
- `README.md`: Added more information and beautified it.

## 🗑️ Delete

- `<package-name>/__version__.py`

---

# v1.0.0

![](https://img.shields.io/badge/Version-v1.0.0-green)

## 🎉 Preliminarily establish the project framework.

## 🎯 Features

- A relatively complete software engineering project structure, including directories for [code](https://github.com/Ahzyuan/Python-package-template/tree/v1.0.0/package-name), [test](https://github.com/Ahzyuan/Python-package-template/tree/v1.0.0/tests), [document](https://github.com/Ahzyuan/Python-package-template/tree/v1.0.0/docs), and [project demonstration](https://github.com/Ahzyuan/Python-package-template/tree/v1.0.0/examples)

- `setup.py` is a collection of useful patterns and best practices. It extends the `python setup.py` command to achieve one-step code updates, package builds, and releases to [PyPi](https://pypi.org/) using `Twine`.