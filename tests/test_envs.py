# -*- coding: utf-8 -*-

from django.test import TestCase
from django_envie.workroom import convertfiletovars

import os


class DjangoEnvieTestCase(TestCase):
    def test_convertfiletovars(self):
        filepath = os.path.join('.env.py')
        with open(filepath, 'w+') as f:
            f.write('SECRET_KEY = "Not so secret"')
        convertfiletovars()
        secret_key = os.getenv('SECRET_KEY')
        self.assertEqual(secret_key, 'Not so secret')
        os.remove(filepath)
        del os.environ['SECRET_KEY']

    def test_convertfiletovars_env_file_outside_project(self):
        filepath = os.path.join('..', '.env.yml')
        with open(filepath, 'w+') as f:
            f.write('secret_key : "Not so secret"\r\nmy_name : "Oluwafemi"')
        convertfiletovars(fileext='yml')
        secret_key = os.getenv('secret_key')
        self.assertEqual(secret_key, 'Not so secret')
        tmp_path = os.path.dirname(os.path.realpath(__file__))
        os.remove(os.path.join(tmp_path, '..', '..', '.env.yml'))
