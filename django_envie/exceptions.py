'''
exceptions.py:
'''

class ParseError(Exception):
    message = '''
    No environment file found in your project directory.
    Go ahead and create one.
    '''
