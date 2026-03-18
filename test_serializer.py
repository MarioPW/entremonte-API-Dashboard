import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from users.serializers import UserSerializer

data = {
    "email": "testuser777@test.com",
    "first_name": "Test",
    "last_name": "User",
    "password": "TestPassword123!",
    "re_password": "TestPassword123!"
}

serializer = UserSerializer(data=data)
if serializer.is_valid():
    print("VALID! Saving...")
    user = serializer.save()
    print("User created:", user)
else:
    print("INVALID:", serializer.errors)
