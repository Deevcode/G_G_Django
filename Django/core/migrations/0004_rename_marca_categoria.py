# Generated by Django 4.0.1 on 2022-05-24 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_producto_imagen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marca',
            new_name='Categoria',
        ),
    ]