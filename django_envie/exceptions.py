'''
exceptions.py:
'''

class ParseError(FileNotFoundError):
    message = '''
    No environment file found in your project directory.
    Go ahead and create one.
    '''
