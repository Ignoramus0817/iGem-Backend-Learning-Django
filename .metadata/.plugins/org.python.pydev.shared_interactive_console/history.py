import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'BlogSys.settings'; import django
if django.VERSION <= (1, 5):
    from django.core import management
    import BlogSys.settings as settings
    management.setup_environ(settings)
else:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
dbshell
python manage.py dbshell
csl
cls
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'BlogSys.settings'; import django
if django.VERSION <= (1, 5):
    from django.core import management
    import BlogSys.settings as settings
    management.setup_environ(settings)
else:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
exit
exit(0)
exit()
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'BlogSys.settings'; import django
if django.VERSION <= (1, 5):
    from django.core import management
    import BlogSys.settings as settings
    management.setup_environ(settings)
else:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
python manage.py createsuperuser
createsuperuser
python
