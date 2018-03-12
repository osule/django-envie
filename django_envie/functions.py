'''
functions.py:
'''
import functools
import os

from .parsers import get_parser
from .exceptions import ParseError


BASE_DIR = os.getcwd()

def inject(env, variables):
    env.update(variables)

def basepath(*args):
    ''' Construct path relative to base directory '''
    return os.path.join(BASE_DIR, *args)

def parse_using(extension):
    return get_parser(extension)

def parse(*args):
    ''' Parses file and sets environment key. '''
    def reduce_fn(cumm, currpath):
        file_extension = currpath.split('.')[-1]
        data, error = parse_using(file_extension)(currpath)

        cumm_data, cumm_error = cumm
        if not error:
            cumm_data.update(data)

        return (cumm_data, cumm_error or error)

    parsed_data, parsed_error = functools.reduce(reduce_fn, args, ({}, False))

    if not parsed_data:
        raise ParseError
    return parsed_data

def load_vars(environ=None):
    '''
    Set environment variables from .env.py or .env.yml
    if it exists in the project dir.
    '''
    environ = environ if environ else os.environ

    try:
        variables = parse(
            basepath('..', '.env.py'),
            basepath('.env.py'),
            basepath('..', '.env.yml'),
            basepath('.env.yml'),
        )
        inject(environ, variables)
    except ParseError as err:
        return err.message
