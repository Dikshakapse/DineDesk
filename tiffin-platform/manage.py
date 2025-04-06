#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# ✅ Add backend to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

# ✅ Correct settings module path (because tiffin_backend is inside backend folder)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tiffin_backend.settings')

def main():
    """Run administrative tasks."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
