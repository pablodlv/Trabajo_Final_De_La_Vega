# Generated by Django 4.2.4 on 2023-09-06 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notas', '0003_rename_autores_nota_autor_remove_autor_apellido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='url',
        ),
        migrations.AlterField(
            model_name='nota',
            name='img_destacada',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/destacadas'),
        ),
    ]
