# Generated by Django 3.2.12 on 2022-03-27 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0006_alter_drivertrucks_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivertrucks',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='truckinfo', to='drivers.drivers'),
        ),
    ]