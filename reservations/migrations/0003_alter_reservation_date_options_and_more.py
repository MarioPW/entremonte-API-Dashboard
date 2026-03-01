from django.db import migrations, models
import django.db.models.deletion

def set_default_cabin(apps, schema_editor):
    Cabin = apps.get_model('cabins', 'Cabin')
    default_cabin = Cabin.objects.first()
    ReservationDate = apps.get_model('reservations', 'Reservation_date')
    for rd in ReservationDate.objects.all():
        rd.cabin = default_cabin
        rd.save()

class Migration(migrations.Migration):

    dependencies = [
        ('cabins', '0011_cabin_review_show'),
        ('reservations', '0002_alter_reservation_cabin_alter_reservation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation_date',
            name='cabin',
            field=models.ForeignKey(to='cabins.cabin', on_delete=django.db.models.deletion.CASCADE, null=True),
        ),
        migrations.RunPython(set_default_cabin),
        migrations.AlterField(
            model_name='reservation_date',
            name='cabin',
            field=models.ForeignKey(to='cabins.cabin', on_delete=django.db.models.deletion.CASCADE),
        ),
    ]
