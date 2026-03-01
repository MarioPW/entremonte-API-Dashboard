from django.db import models
import uuid
from django.conf import settings

class Cabin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    available = models.BooleanField(verbose_name='Disponible', default=True)
    price = models.IntegerField(verbose_name='Precio Noche', default=0, unique=False)
    name = models.CharField(verbose_name='Nombre', max_length=50, unique=True, default='Cabaña')
    description = models.TextField(verbose_name='Descripcion', max_length=500, blank=True)
    capacity = models.IntegerField(verbose_name='Capacidad', default=0, unique=False)
    images = models.ManyToManyField('Cabin_image', verbose_name='Imagenes', blank=True, related_name='cabins')
    services = models.ManyToManyField('Cabin_service', verbose_name='Servicios', blank=True, related_name='cabins')
    reviews = models.ManyToManyField('Cabin_review', verbose_name='Comentarios', blank=True, related_name='cabins')

    def __str__(self):
        return self.name
    def get_services(self):
        return ", ".join(self.services.values_list("name", flat=True))
    def get_images(self):
        return ", ".join(self.images.values_list("image", flat=True))
    def get_reviews(self):
        return ", ".join(self.reviews.values_list("comment", flat=True))
    class Meta:
        verbose_name_plural = "Cabañas"

class Cabin_service(models.Model):
    id    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField( max_length=50, unique=True, verbose_name='Servicio')
    class Meta:
        verbose_name_plural = "Servicios de Cabañas"

    def __str__(self):
        return self.name

class Cabin_image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField( max_length=50, unique=True, verbose_name='Nombre')
    image = models.FileField(upload_to='cabin_images', verbose_name='Imagen')

    class Meta:
        verbose_name_plural = "Imagenes de Cabañas"
    def __str__(self):
        return self.name

class Cabin_review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name='Calificacion', default=0)
    comment = models.TextField(verbose_name='Comentario', max_length=500, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    show = models.BooleanField(verbose_name='Mostrar', default=False)

    class Meta:
        verbose_name_plural = "Comentarios de Cabañas"
