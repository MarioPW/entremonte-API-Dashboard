from django.db import models
from django.db.models.fields.related import ForeignKey
import uuid

class Slider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, verbose_name='Titulo', default='Titulo', blank=True)
    url = models.FileField(verbose_name='Url',upload_to='Slider_images', blank=False)

    class Meta:
        verbose_name_plural = 'Slider Principal'