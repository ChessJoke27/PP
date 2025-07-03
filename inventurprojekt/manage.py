#!/usr/bin/env python3
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventurprojekt.settings')
    from django.core.management import execute_from_command_line, call_command

    if 'runserver' in sys.argv:
        try:
            call_command('migrate', interactive=False)
        except Exception as exc:
            print(f'Could not run migrations: {exc}')

    execute_from_command_line(sys.argv)
