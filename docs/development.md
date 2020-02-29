
# DEVELOPERS

This section of the documentation covers all the notions needed to play and hack with the GTL core code.

# Prerequisites

- Python 3.7 and greater
- poetry

The unique tool you need to manage and hack the GTL project is poetry.
Poetry is a tool for dependency management and packaging in Python.
It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

The documentation about poetry is available on the site [https://python-poetry.org/](https://python-poetry.org/) where
you can find how to install it for any platform.

# 🚀Getting started

```bash
git clone https://github.com/tipipigri/GTL
cd GTL
poetry install
```

## Install the git hooks
Git hooks are automated check and scripts that prevent common code errors and help to follow standards and other
amenities before any commit to the repo by running also tests and linting.

Install them is easy as:

```bash
poetry run task hook
```

# Other tasks

### linting
```bash
poetry run task lint
```

### test
```bash
poetry run task test
```

### lint and test
```bash
poetry run task verify
```

### IDE help
Sometimes IDE (like pycharm) need the path of the virtualenv to autolink the dependencies and make the completions work.

#### [PyCharm](https://www.jetbrains.com/pycharm/)
Follow this thread https://youtrack.jetbrains.com/issue/PY-30702

```bash
poetry env info -p
poetry run which python
ln -s (poetry env info -p) .venv
```
or set forever the
```bash
poetry config virtualenvs.in-project true
```

#### [Code](https://code.visualstudio.com/)

Follow [this](https://devblogs.microsoft.com/python/python-in-visual-studio-code-march-2019-release/)

# Documentation

The documentation is handled with [docsify](https://docsify.js.org/) and within the `docs/` folder of the root project.

Preview of the documentation on localhost:

```bash
docsify ./docs
```
