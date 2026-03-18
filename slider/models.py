from django.db import models
import uuid

class Slider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, verbose_name='Titulo', default='Titulo', blank=True)
    url = models.FileField(verbose_name='Url',upload_to='Slider_images', blank=False)
    message = models.CharField(max_length=100, verbose_name='Mensaje', default='', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Slider Principal'