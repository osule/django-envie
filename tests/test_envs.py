# -*- coding: utf-8 -*-

from django.test import TestCase
from django_envie.workroom import convertfiletovars, BASE_DIR, Config

import os


class DjangoEnvieTestCase(TestCase):
    def test_py_inside_project(self):
        """Test that a config file inside of the project folder
        with the .py extension is detected
        """
        filepath = os.path.join('.env.py')
        with open(filepath, 'w+') as f:
            f.write('SECRET_KEY = "Not so secret"')
        convertfiletovars()
        secret_key = os.getenv('SECRET_KEY')
        self.assertEqual(secret_key, 'Not so secret')
        os.remove(filepath)
        del os.environ['SECRET_KEY']

    def test_yml_inside_project(self):
        """Test that a config file inside the project folder
        with the .yml extension is detected
        """
        filepath = os.path.join('.env.yml')
        with open(filepath, 'w+') as f:
            f.write('SECRET_KEY : "Not so secret"')
        convertfiletovars()
        secret_key = os.getenv('SECRET_KEY')
        self.assertEqual(secret_key, 'Not so secret')
        os.remove(filepath)
        del os.environ['SECRET_KEY']

    def test_py_outside_project(self):
        """Test that a config file outside of the project folder
        with the .py extension is detected
        """
        filepath = os.path.join(BASE_DIR, '..', '.env.py')
        with open(filepath, 'w+') as f:
            f.write('SECRET_KEY = "Not so secret"')
        convertfiletovars()
        secret_key = os.getenv('SECRET_KEY')
        self.assertEqual(secret_key, 'Not so secret')
        os.remove(filepath)
        del os.environ['SECRET_KEY']

    def test_yml_outside_project(self):
        """Test that a config file outside of the project folder
        with the .py extension is detected
        """
        filepath = os.path.join(BASE_DIR, '..', '.env.yml')
        with open(filepath, 'w+') as f:
            f.write('SECRET_KEY : "Not so secret"')
        convertfiletovars()
        # import pdb; pdb.set_trace()
        secret_key = os.getenv('SECRET_KEY')
        self.assertEqual(secret_key, 'Not so secret')
        os.remove(filepath)
        del os.environ['SECRET_KEY']

    def test_error_is_raised_when_no_config_file(self):
        """Test that an error message is returned when a config
        file isn't present
        """
        pyfilepath = os.path.join(BASE_DIR, '.env.py')
        ymlfilepath = os.path.join(BASE_DIR, '.env.yml')
        self.assertEqual(IOError, type(Config.parse_file(pyfilepath)))
        self.assertEqual(IOError, type(Config.parse_file(ymlfilepath)))
        pyfilepath = os.path.join(BASE_DIR, '..', '.env.py')
        ymlfilepath = os.path.join(BASE_DIR, '..', '.env.yml')
        self.assertEqual(IOError, type(Config.parse_file(pyfilepath)))
        self.assertEqual(IOError, type(Config.parse_file(ymlfilepath)))
        res = convertfiletovars()
        self.assertIn('No environment file', res)
