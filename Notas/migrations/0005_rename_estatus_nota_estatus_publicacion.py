# Generated by Django 4.2.4 on 2023-09-06 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notas', '0004_remove_nota_url_alter_nota_img_destacada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nota',
            old_name='estatus',
            new_name='estatus_publicacion',
        ),
    ]
