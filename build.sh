#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Recopilar archivos estáticos
# Necesario para que WhiteNoise sirva tus CSS/JS en Render
python manage.py collectstatic --no-input

# 3. Aplicar migraciones
# Solo aplicamos las migraciones que ya existen en tu código (enviadas por Git)
python manage.py migrate

# 4. Creación de superusuario (Opcional/Segura)
# El flag || true evita que el script falle si el usuario ya existe.
# Ya NO borramos al usuario antes de este paso.
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
email = '$DJANGO_SUPERUSER_EMAIL';
password = '$DJANGO_SUPERUSER_PASSWORD';
if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(email=email, password=password, first_name='Admin')
    print('Usuario creado con éxito')
else:
    user = User.objects.get(email=email)
    user.set_password(password)
    user.save()
    print('Password de usuario actualizado')
"