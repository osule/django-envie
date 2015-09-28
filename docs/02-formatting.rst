Formatting your configuration
=============================

The format specified below is typical of what you should have in your .env.py file.

You can place the .env.py file outside of your django project folder to keep up with best practices.

     .. code-block:: python

        DBNAME = "sector_seven"
        DB_USER = "homer_simpson"
        DB_PASSWORD = "Close, but you're way off."

For a .env.yml file, you can specify your configuration in the following format.

    .. code-block::

        secret_key:
            'not so secret'
        api_token:
            'bleblebleblebleh'