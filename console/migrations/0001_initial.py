# Generated by Django 4.1.3 on 2022-12-11 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(blank=True, max_length=256, verbose_name='Date and Time')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.package', verbose_name='Package')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]