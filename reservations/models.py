from django.db import models
from django.conf import settings
from carta.models import Item
from cabins.models import Cabin
import uuid

class Reservation_date(models.Model):
    date = models.DateField(verbose_name="Fecha de Reserva")
    cabin = models.ForeignKey(Cabin, on_delete=models.CASCADE, verbose_name="Cabaña", null=True)
    available = models.BooleanField(verbose_name="Habilitada", default=True)

    class Meta:
        verbose_name_plural = "Habilitar Fechas"
        unique_together = ['date', 'cabin']

    def __str__(self):
        return f"Reserva para {self.cabin.name} el {self.date}"


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuario')
    date = models.ForeignKey(Reservation_date, on_delete=models.CASCADE, verbose_name='Fecha de Reserva')
    cabin = models.ForeignKey(Cabin, on_delete=models.CASCADE, verbose_name='Cabaña')
    dishes_order1 = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name='reservation_item1', verbose_name='Menú 1')
    dishes_order2 = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name='reservation_item2', verbose_name='Menú 2')

    class Meta:
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva de {self.user.email} el {self.date.date} en {self.cabin.name}"


class Reservation_request(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuario')
    checkin = models.DateField(verbose_name="Fecha de Llegada")
    checkout = models.DateField(verbose_name="Fecha de Salida")
    user_phone = models.CharField(max_length=15, verbose_name="Teléfono del Usuario", default='', blank=True)
    date = models.DateField(verbose_name="Fecha de Solicitud", auto_now_add=True)
    approved = models.BooleanField(default=False, verbose_name="Aprobar Solicitud")

    class Meta:
        verbose_name_plural = "Solicitudes de Reserva"
        unique_together = ['date']

    def __str__(self):
        return f"Solicitud de {self.user.email} para el {self.date}"