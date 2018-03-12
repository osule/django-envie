import re
import os

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name="django-envie",
    version="1.0.0",
    description="A module for Django that allows your app to"
    " use environment variables in a file",
    long_description="Django-envie helps your Django app to be"
    " aware of environment variables set in a .py or .yml file.",
    author="Oluwafemi Sule",
    author_email="oluwafemisule@outlook.com",
    url="https://github.com/osule/django-envie",
    download_url="https://github.com/osule/django-envie.git",
    license="MIT License",
    packages=[
        "django_envie",
    ],
    include_package_data=True,
    install_requires=[
        "Django>=1.8.0,<2.0.0",
        "PyYAML>=3.11"
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        "pytest",
        "pytest-cov",
        "pytest-ordering",
        "coverage",
    ],
    zip_safe=False,
    test_suite="tests.runtests.start",
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
