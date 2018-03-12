# -*- coding: utf-8 -*-

import os
import pytest

from django_envie import basepath, parse, load_vars
from django_envie.exceptions import ParseError


@pytest.fixture(
    scope="session",
    params=[
        ('.env.py',),
        ('.env.yml',),
        ('..', '.env.py',),
        ('..', '.env.yml',),
    ])
def configfile(request):
    filepath = basepath(*request.param)
    
    yield filepath

    os.remove(filepath)
    del os.environ['SECRET_KEY']

@pytest.mark.second
def test_configfile(configfile):
    """Test that a config file is detected
    """
    is_yml = configfile.endswith('.yml')

    with open(configfile, 'w') as file:
        if is_yml:
            file.write('SECRET_KEY : "Not so secret"')
        else:
            file.write('SECRET_KEY = "Not so secret"')
    load_vars()

    assert os.getenv('SECRET_KEY') == 'Not so secret'

@pytest.mark.first
def test_raising_error_for_missing_config_file():
    """Test that an error message is returned when a config
    file isn't present
    """
    pyfilepath = basepath('.env.py')
    pytest.raises(ParseError, parse, pyfilepath)

    ymlfilepath = basepath('.env.yml')
    pytest.raises(ParseError, parse, ymlfilepath)

    pyfilepath = basepath('..', '.env.py')
    pytest.raises(ParseError, parse, ymlfilepath)

    ymlfilepath = basepath('..', '.env.yml')
    pytest.raises(ParseError, parse, pyfilepath)
