'''
parsers.py:
'''
import os
import re

import yaml


def parse_ymlfile(filepath):
    try:
        with open(filepath, 'r') as configfile:
            return yaml.load(configfile), None
    except (IOError, ValueError) as exc:
        return exc, True


def parse_pyfile(filepath):
    try:
        with open(filepath, 'r') as configfile:
            dct = {}
            for setting in configfile:
                match = re.search(r'(\w+)\s=\s[\"|\'](.*?)[\"|\']', setting)
                key, value = match.groups()
                dct[key] = value
            return dct, None
    except (IOError, ValueError) as exc:
        return exc, True

PARSERS = {
    'yml': parse_ymlfile,
    'py': parse_pyfile,
}
def get_parser(extension):
    return PARSERS.get(extension)
