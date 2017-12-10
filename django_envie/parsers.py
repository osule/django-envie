'''
parsers.py:
'''
import os
import re

import yaml


def parse_ymlfile(filepath):
    status, err = True, None
    try:
        with open(filepath, 'r') as configfile:
            environ_data = yaml.load(configfile)
            for key, value in environ_data.iteritems():
                os.environ.update({key: value})
    except (IOError, ValueError) as exc:
        status, err = False, exc
    return status, err


def parse_pyfile(filepath):
    status, err = True, None
    try:
        with open(filepath, 'r') as configfile:
            for setting in configfile:
                match = re.search(r'(\w+)\s=\s[\"|\'](.*?)[\"|\']', setting)
                key, value = match.groups()
                os.environ.update({key: value})
    except (IOError, ValueError) as exc:
        status, err = False, exc
    return status, err


PARSERS = {
    'yml': parse_ymlfile,
    'py': parse_pyfile,
}
def get_parser(extension):
    return PARSERS.get(extension)
