# Generated by Django 3.2.20 on 2023-08-02 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_busket_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fields',
            options={'verbose_name': 'Fields', 'verbose_name_plural': 'Fields'},
        ),
        migrations.AlterField(
            model_name='busket',
            name='image_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]