from re import search
import os

BASE_DIR = os.getcwd()


class Config():
    ERROR = """
    No environment file found in your project directory.
    Go ahead and create one.
    """
    PYFILEPATH = os.path.join(BASE_DIR, '.env.py')
    YAMLFILEPATH = os.path.join(BASE_DIR, '.env.yml')

    @staticmethod
    def is_file(file_path):
        """Checks that a file exists"""
        return os.path.isfile(file_path)

    @staticmethod
    def up_one_level(file_ext):
        """Goes up one level in the directory"""
        return os.path.join(BASE_DIR, '..', file_ext)

    @staticmethod
    def parse_file(file_path):
        """Parses file and sets environment key"""
        file_extension = file_path.split('.')[-1]

        if file_extension == 'py':
            try:
                pyfile = open(file_path, 'r')
                for setting in pyfile.readlines():
                    match = search("(\w+)\s=\s\"(.*?)\"", setting)
                    key, value = match.groups()
                    os.environ.update({key: value})
                return True
            except Exception as e:
                return e

        elif file_extension == 'yml':
            from yaml import load
            try:
                environ_data = load(file(file_path, 'r'))
                for key, value in environ_data.iteritems():
                    os.environ.update({key: value})
                return True
            except Exception as e:
                return e


def convertfiletovars():
    """
    Set environment variables from .env.py or .env.yml
    if it exists in the project dir.
    """
    FLAG_ERROR = False
    FLAG_SUCCEED = False

    while not FLAG_ERROR:
        if FLAG_SUCCEED is True:  # quick break out of loop
            break
        if Config.is_file(Config.PYFILEPATH):  # does a .env.py file exist
            FLAG_SUCCEED = Config.parse_file(Config.PYFILEPATH)
        elif Config.is_file(Config.YAMLFILEPATH):  # does a .env.yml file exist
            FLAG_SUCCEED = Config.parse_file(Config.YAMLFILEPATH)
        else:
            pyfilepath = Config.up_one_level('.env.py')  # up one level
            yamlfilepath = Config.up_one_level('.env.yml')  # up one level
            if Config.is_file(pyfilepath):
                FLAG_SUCCEED = Config.parse_file(pyfilepath)
            elif Config.is_file(yamlfilepath):
                FLAG_SUCCEED = Config.parse_file(yamlfilepath)
            elif not Config.is_file(pyfilepath) and not Config.is_file(
                 yamlfilepath):
                FLAG_ERROR = True

    if FLAG_ERROR:
        return Config.ERROR
