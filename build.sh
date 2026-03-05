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
if [ "$DJANGO_SUPERUSER_EMAIL" ]; then
    python manage.py createsuperuser \
        --noinput \
        --email "$DJANGO_SUPERUSER_EMAIL" || true
fi