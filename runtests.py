#!/usr/bin/env python
import sys
from os.path import dirname, abspath
from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS = [
            'tests.testapp',
        ],
        CACHES = {
            'default': {
                'BACKEND': 'dredis_cache.RedisCache',
                'LOCATION': [
                    '127.0.0.1:6379',
                    '127.0.0.1:6380',
                    '127.0.0.1:6381',
                    '127.0.0.1:6382',
                ],
                'OPTIONS': {
                    'DB': 15,
                    'PASSWORD': 'yadayada',
                },
            },
        }
    )

from django.test.simple import DjangoTestSuiteRunner

def runtests(*test_args):
    if not test_args:
        test_args = ['testapp']
    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    runner = DjangoTestSuiteRunner(verbosity=1, interactive=True, failfast=False)
    failures = runner.run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])
