from re import search
import os


def convertfiletovars(fileext='py'):
    """
    Set environment variables from .env.py
    if it exists in the project dir.
    """

    filepath = os.path.join(os.getcwd(), '.env.'+fileext)
    if not os.path.isfile(filepath):
        # Backtrack to root directory
        os.chdir('..')
        filepath = os.path.join('.env.'+fileext)
    if os.path.isfile(filepath):
        if fileext == 'py':
            try:
                with open(filepath, 'r') as env_file:
                    for setting in env_file:
                        match = search("(\w+)\s=\s\"(.*?)\"", setting)
                        env_var, config = match.groups()
                        os.environ[env_var] = config
            except:
                print "No .env.py environment file found in your project directory.\
                Go ahead and create one."
        elif fileext == 'yml':
            from yaml import load
            try:
                environ_data = load(file(filepath, 'r'))
                for key, value in environ_data.iteritems():
                    os.environ[key] = value
            except:
                print "No .env.yaml environment file found in your project directory.\
                Go ahead and create one."
