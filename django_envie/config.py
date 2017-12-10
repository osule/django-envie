'''
config.py:
'''
import functools
import os

from .parsers import get_parser
from .exceptions import ParseError


BASE_DIR = os.getcwd()


def is_file(filepath):
    ''' Checks that a file exists. '''
    return os.path.isfile(filepath)

def basepath(*args):
    ''' Construct path relative to base directory '''
    return os.path.join(BASE_DIR, *args)


class Config():
    @classmethod
    def parse_using(cls, extension):
        parser_fn = get_parser(extension)

        def parse_fn(filepath):
            return parser_fn(filepath)

        return parse_fn

    @classmethod
    def parse(cls, *args):
        ''' Parses file and sets environment key. '''
        def reduce_fn(cumm, currpath):
            file_extension = currpath.split('.')[-1]
            status, _ = cls.parse_using(file_extension)(currpath)
            return cumm or status

        parsed = functools.reduce(reduce_fn, args, False)

        if not parsed:
            raise ParseError

def file_to_env():
    '''
    Set environment variables from .env.py or .env.yml
    if it exists in the project dir.
    '''

    try:
        Config.parse(
            basepath('.env.yml'),
            basepath('..', '.env.yml'),
            basepath('.env.py'),
            basepath('..', '.env.py'),
        )
    except ParseError as err:
        return err.message
