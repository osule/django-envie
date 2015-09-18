# -*- coding: utf-8 -*-

from django.test import TestCase
from django_envie.workroom import convertfiletovars

import os


class DjangoEnvieTestCase(TestCase):
    def test_convertfiletovars(self):
        convertfiletovars()
        secret_key = os.getenv('SECRET_KEY')
        self.assertEqual(secret_key, 'Not so secret')
