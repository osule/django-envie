How to use this module
======================

It is easy to get started with this module.

First, install this module in your virtual environment or base python installation.

.. code-block:: none
    
    pip install django_envie


At the top of your Django project settings file, add the following code blocks.


.. code-block:: python

    from django_envie.workroom import convertfiletovars
    import os

    convertfiletovars()

If you're making use of a .yml file for your configuration, call convertfiletovars as below:

.. code-block:: python

    convertfiletovars(fileext='yml') 


Finally, you can access set environment variables by doing the following in your project settings file.

.. code-block:: python

    SECRET_KEY = os.getenv('SECRET_KEY')


