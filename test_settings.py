import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
try:
    from django.conf import settings
    django.setup()
    print("DEBUG =", settings.DEBUG)
    print("ALLOWED_HOSTS =", settings.ALLOWED_HOSTS)
    print("DATABASES =", settings.DATABASES)
except Exception as e:
    print(f"FAILED: {type(e).__name__}: {e}")
