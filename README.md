# Django-Envie

[![travis-ci]][travis]
[![pypi-version-image]][pypi]

This module helps to set environment variable for your Django application from a _.env.py_ or _.env.yml_ file placed inside the project directory.

## Installation
```
pip install django-envie
```

## Usage
To use, create an environment file, save as either a _.env.py_ or _.env.yml_ file format in your django project (inside the project directory) or repository root (outside the project directory).

## Configuration
The _.env.py_ file for a django project should be formatted this way:
```python
DB_NAME = "sector_seven"
DB_USER = "homer_simpson"
DB_PASSWORD = "Close, but you're way off."
```

If using _.env.yml_ file format
```
DB_NAME: "sector_seven"
DB_USER: "homer_simpson"
DB_PASSWORD: "Close, but you're way off."
```

In the project settings script, include this snippet:
```python
from django_envie.workroom import convertfiletovars

convertfiletovars()
```

## Accessing your environment variables
Accessing environment variables anywhere can be done by using
```python
os.getenv('DB_NAME')
```
## Setting up your environment variable for Continuous Integration
### CircleCI
```
KEY = SECRET_KEY
VALUE = my secret key
```
### TravisCI
```
KEY = SECRET_KEY
VALUE = "my secret key"
```

Checkout the documentation for this project [here](http://django-envie.readthedocs.org/en/latest/)

[travis-ci]: https://travis-ci.org/RainbowSeven/django-envie.svg?branch=master
[travis]: https://travis-ci.org/RainbowSeven/django-envie?branch=master
[pypi-version-image]: https://img.shields.io/pypi/v/django_envie.svg
[pypi]: https://pypi.python.org/pypi/django-envie