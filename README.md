## 📦 A Project Template for Self-developed Python Package

![Static Badge](https://img.shields.io/badge/Version-v1.0.1-green)
[![Static Badge](https://img.shields.io/badge/License-MIT-khaki)](https://opensource.org/license/MIT)
![Static Badge](https://img.shields.io/badge/PyPi-Package_pattern-yellow?logo=pypi&labelColor=%23FAFAFA)

[![Static Badge](https://img.shields.io/badge/Build-setuptools-red)](https://github.com/pypa/setuptools)
[![Static Badge](https://img.shields.io/badge/Formatter-Ruff-sienna?logo=ruff)](https://github.com/astral-sh/ruff)
[![Imports: isort](https://img.shields.io/badge/%20Imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

---

- This repo is inspired by https://github.com/navdeep-G/setup.py, aiming to boot up your develop speed when you are creating a new Python package.  

- This repo is modified from the [origin repo](https://github.com/navdeep-G/setup.py) in strict accordance with the requirements of its license, and still adhere to the principle of open source sharing.

---

This repo exists to provide a project structure template,   
which can be used to accelerate the development of a Python third-party package.

## 🎯 Features

- 𝐀 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞 𝐩𝐫𝐨𝐣𝐞𝐜𝐭 𝐬𝐭𝐫𝐮𝐜𝐭𝐮𝐫𝐞 that complies with software engineering specifications. 
    <details>
    <summary>𝖯𝗋𝗈𝗃𝖾𝖼𝗍 𝗌𝗍𝗋𝗎𝖼𝗍𝗎𝗋𝖾 𝖾𝗑𝗉𝗅𝖺𝗇𝖺𝗍𝗂𝗈𝗇</summary>

    ```
    Python-package-template/
    ├── tests/           # Storage unit test code
    ├── docs/            # Store document related files
    ├── examples/        # Store project demo code
    ├── package-name/    # Store project code
    │   ├── core.py      # Core code
    │   └── __init__.py  # Package initialization file, defining copyright, version, and other information
    ├── LICENSE          # Project license
    ├── MANIFEST.in      # Describe the files included or not included in build package
    ├── CHANGELOG.md     # Project changelog
    ├── README.md        # Project description
    ├── requirements.txt # Project dependency
    ├── ruff.toml        # Define rules for code style, code inspection, and import management
    └── setup.py         # Project packaging script
    ```

    </details>

- 𝐀 𝐟𝐮𝐥𝐥𝐲 𝐜𝐨𝐧𝐟𝐢𝐠𝐮𝐫𝐞𝐝 [`𝐬𝐞𝐭𝐮𝐩.𝐩𝐲`](setup.py)

  - **𝖶𝖾𝗅𝗅 𝖼𝗈𝗆𝗆𝖾𝗇𝗍𝖾𝖽**: no need to look up [documents]((https://setuptools.pypa.io/en/latest/references/keywords.html)) to understand each metadata's meaning, comments are provided for most of them. 
  - **𝖣𝗒𝗇𝖺𝗆𝗂𝖼 𝗆𝖾𝗍𝖺𝖽𝖺𝗍𝖺**: allows dynamic matching of update information when building packages, including `version`, `README`, and project dependencies.

- 𝐄𝐟𝐟𝐢𝐜𝐢𝐞𝐧𝐭 𝐚𝐧𝐝 𝐬𝐭𝐚𝐧𝐝𝐚𝐫𝐝: We use the wonderful Python linter and code formatter [`Ruff`](https://github.com/astral-sh/ruff) to ensure code quality and maintainability

> Note: We use `setup.py` to manage all metadata, and discard `setup.cfg`. Cause the latter can't dynamically solve the value of metadata. Meanwhile, we leave all the work of code checking and import management to awesome [`Ruff`](https://github.com/astral-sh/ruff), i.e., using [`ruff.toml`](ruff.toml).

## 🔨 Usage

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
- [x] Add linter

## 👀 See More

- [What is setup.py?](https://stackoverflow.com/questions/1471994/what-is-setup-py)
- [Official Python Packaging User Guide](https://packaging.python.org)
- [Setuptools User Guide](https://setuptools.pypa.io/en/latest/userguide/index.html)
- [The Hitchhiker's Guide to Packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html)
- [Cookiecutter template for a Python package](https://github.com/audreyr/cookiecutter-pypackage)
- [isort document](https://pycqa.github.io/isort/index.html)
- [Ruff document](https://docs.astral.sh/ruff/)

# 🧾 License

This is free and unencumbered software released into the public domain, modified from https://github.com/navdeep-G/setup.py. Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.