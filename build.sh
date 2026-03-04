#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Recopilar archivos estáticos
python manage.py collectstatic --no-input

# 3. Generar migraciones (Primero users para evitar el ValueError de dependencias)
python manage.py makemigrations users
python manage.py makemigrations

# 4. Aplicar las migraciones a la base de datos de Render
python manage.py migrate

# 4. Crear superusuario (Solo si las variables están presentes)
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
    python manage.py createsuperuser \
        --noinput \
        --username "$DJANGO_SUPERUSER_USERNAME" \
        --email "$DJANGO_SUPERUSER_EMAIL" || true
fi