from re import search
import os


BASE_DIR = os.getcwd()

ERROR = "No environment file found in your project directory. Go ahead and create one."

PYENV = '.env.py'
YAMLENV = '.env.yml'


def convertfiletovars():
    """
    Set environment variables from .env.py or .env.yml
    if it exists in the project dir.
    """
    FLAG_ERROR = False
    res = None
    # check if env.py exists
    pyfilepath = os.path.join(BASE_DIR, PYENV)
    yamlfilepath = os.path.join(BASE_DIR, YAMLENV)
    if os.path.isfile(pyfilepath):
        res = parse_file(pyfilepath)
    elif os.path.isfile(yamlfilepath):
        res = parse_file(yamlfilepath)
    else:
        # Backtrack to root directory
        pyfilepath = os.path.join(BASE_DIR, '..', PYENV)
        yamlfilepath = os.path.join(BASE_DIR, '..', YAMLENV)
        if os.path.isfile(pyfilepath):
            res = parse_file(pyfilepath)
        elif os.path.isfile(yamlfilepath):
            res = parse_file(yamlfilepath)
        elif not os.path.isfile(pyfilepath) and not os.path.isfile(yamlfilepath):
            FLAG_ERROR = True

    if FLAG_ERROR is True:
        print ERROR
    if res:
        print res.message


def parse_file(file_path):
    file_extension = file_path.split('.')[-1]

    if file_extension == 'py':
        try:
            pyfile = open(file_path, 'r')
            for setting in pyfile.readlines():
                match = search("(\w+)\s=\s\"(.*?)\"", setting)
                key, value = match.groups()
                os.environ.update({key: value})
        except Exception as e:
            return e

    elif file_extension == 'yml':
        from yaml import load
        try:
            environ_data = load(file(file_path, 'r'))
            for key, value in environ_data.iteritems():
                os.environ.update({key: value})
        except Exception as e:
            return e
