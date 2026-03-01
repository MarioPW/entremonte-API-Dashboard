from django.db import models
from django.db.models.fields.related import ForeignKey
import uuid

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(verbose_name='Categoría', max_length=50, unique=True)
    possition = models.IntegerField(verbose_name='Posción', default=0, unique=True)
    available = models.BooleanField(verbose_name='Disponible', default=True)

    class Meta:
        verbose_name_plural = 'Categorías'
        ordering = ['possition']
   
    def __str__(self) -> str:
        return self.category

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Nombre', max_length=50, unique=True)
    category = ForeignKey(Category, on_delete=models.CASCADE, null=False)
    description = models.TextField(verbose_name='Descripcion', max_length=500, blank=True)
    price = models.IntegerField(verbose_name='Precio', default=0, unique=False)
    available = models.BooleanField(verbose_name='Disponible', default=True)
    image = models.FileField(verbose_name='Imagen',upload_to='Item_images', default='default_item_image')
    created_at = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Carta Items'
    
    def __str__(self) -> str:
        return self.name
