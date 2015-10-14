Django-Envie
============

This module helps to set environment variable for your Django application from a _.env.py_ file placed inside the project directory.

You can also place your _.env.py_ outside of the project directory where you have your _.git_ folder if you're using git for version control.


Installation
------------
```
pip install django-envie
```

An environment file (_.env.py_ or .env.yml_) is created either in your django project (inside the project directory) or repository root (outside the project directory).


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

Checkout the documentation for this project [here](http//:django-envie.readthedocs.org "Read the documentation")
