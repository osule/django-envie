import os
import sys
import pytest


def start(argv=None):
    sys.exitfunc = lambda: sys.stderr.write("Shutting down...\n")

    if argv is None:
        argv = [
            "py.test", "---cov=django_envie", "tests/"
        ]

    pytest.main([argv, os.path.abspath(os.path.dirname(__file__))])


if __name__ == "__main__":
    start(sys.argv)
