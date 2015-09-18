How to use this module
======================

It is easy to get started with this module.

First, install this module in your virtual environment or base python installation.

.. code-block:: none
    
    pip install django_envie


At the top of your Django project settings file, add the following code blocks.


.. code-block:: python

    from django_envie.workroom import convertfiletovars()
    import os

    convertfiletovars()


Finally, your can access set environment variables by doing using the following.

.. code-block:: python

    SECRET_KEY = os.getenv('SECRET_KEY')

