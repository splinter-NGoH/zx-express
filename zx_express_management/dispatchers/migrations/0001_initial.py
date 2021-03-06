# Generated by Django 3.2.12 on 2022-03-30 01:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DispatcherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('birthdate', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=254)),
                ('start_shift', models.CharField(max_length=254)),
                ('end_shift', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dispatcher Profile',
                'verbose_name_plural': 'Dispatchers Profile',
            },
        ),
        migrations.CreateModel(
            name='DispatchersAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dispatcher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dispatchers_announcements', to='dispatchers.dispatcherprofile')),
            ],
            options={
                'verbose_name': 'Dispatcher Announcement',
                'verbose_name_plural': 'Dispatchers Announcement',
            },
        ),
    ]
