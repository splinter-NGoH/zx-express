# Generated by Django 3.2.12 on 2022-03-30 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dispatchers', '0001_initial'),
        ('drivers', '0007_alter_drivertrucks_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivers',
            name='dispatchers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drivers_with_dispatcher', to='dispatchers.dispatcherprofile'),
        ),
    ]
