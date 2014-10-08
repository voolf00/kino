import os
import sys

path = '/home/ubuntu/virtualenvs/p-k-kino/kino'

if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_STTINGS_MODUL'] = 'kKino.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()