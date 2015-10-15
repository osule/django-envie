Django-Envie ![Build badge](https://travis-ci.org/RainbowSeven/django-envie.svg?branch=master)
============

This module helps to set environment variable for your Django application from a _.env.py_ or _.env.yml_ file placed inside the project directory.

An environment file (_.env.py_ or .env.yml_) is created either in your django project (inside the project directory) or repository root (outside the project directory).


Installation
------------
```
pip install django-envie
```


Configuration
-------------
The _.env.py_ file for a django project should be formatted this way:
```
DB_NAME = "sector_seven"
DB_USER = "homer_simpson"
DB_PASSWORD = "Close, but you're way off."
```

In the project settings script, include this snippet:
```
from django_envie.workroom import convertfiletovars


convertfiletovars()
```

Use
----
Accessing environment variables anywhere can be done by using
```
os.getenv('DB_NAME')
```

Checkout the documentation for this project [here](http://django-envie.readthedocs.org/en/latest/)
