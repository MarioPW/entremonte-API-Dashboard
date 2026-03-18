import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from djoser.serializers import UserCreateSerializer
from users.serializers import UserSerializer

print("Djoser:")
print(repr(UserCreateSerializer()))
