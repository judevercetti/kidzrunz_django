# Generated by Django 4.1.3 on 2023-03-02 20:47

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_news_alter_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=website.models.gallery_directory_path),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default='oi', max_length=256, verbose_name='Name'),
            preserve_default=False,
        ),
    ]