from re import search
import os


def convertfiletovars():
    """
    Set environment variables from .env.py
    if it exists in the project dir.
    """
    filepath = os.path.join(os.getcwd(), '.env.py')
    if not os.path.isfile(filepath):
        # Backtrack to root directory
        os.chdir('..')
        filepath = os.path.join('.env.py')
    if os.path.isfile(filepath):
        with open(filepath, 'r') as env_file:
            for setting in env_file:
                match = search("(\w+)\s=\s\"(.*?)\"", setting)
                env_var, config = match.groups()
                os.environ[env_var] = config

if __name__ == '__main__':
    convertfiletovars()
