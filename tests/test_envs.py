# -*- coding: utf-8 -*-

from django.test import TestCase
from django_envie.workroom import convertfiletovars, BASE_DIR

import os


class DjangoEnvieTestCase(TestCase):
    def test_py_inside_project(self):
        filepath = os.path.join('.env.py')
        with open(filepath, 'w+') as f:
            f.write('SECRET_KEY = "Not so secret"')
        convertfiletovars()
        secret_key = os.getenv('SECRET_KEY')
        self.assertEqual(secret_key, 'Not so secret')
        os.remove(filepath)
        del os.environ['SECRET_KEY']

    def test_yml_inside_project(self):
        filepath = os.path.join('.env.yml')
        with open(filepath, 'w+') as f:
            f.write('SECRET_KEY : "Not so secret"')
        convertfiletovars()
        secret_key = os.getenv('SECRET_KEY')
        self.assertEqual(secret_key, 'Not so secret')
        os.remove(filepath)
        del os.environ['SECRET_KEY']

    def test_py_outside_project(self):
        filepath = os.path.join(BASE_DIR, '..', '.env.py')
        with open(filepath, 'w+') as f:
            f.write('SECRET_KEY = "Not so secret"')
        convertfiletovars()
        secret_key = os.getenv('SECRET_KEY')
        self.assertEqual(secret_key, 'Not so secret')
        os.remove(filepath)
        del os.environ['SECRET_KEY']

    def test_yml_outside_project(self):
        filepath = os.path.join(BASE_DIR, '..', '.env.yml')
        with open(filepath, 'w+') as f:
            f.write('SECRET_KEY : "Not so secret"')
        convertfiletovars()
        # import pdb; pdb.set_trace()
        secret_key = os.getenv('SECRET_KEY')
        self.assertEqual(secret_key, 'Not so secret')
        os.remove(filepath)
        del os.environ['SECRET_KEY']

    def test_an_error_msg_when_no_yml(self):
        res = convertfiletovars()
        self.assertIn('No environment file', res)
