# Generated by Django 4.1.3 on 2023-07-26 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_package_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
