# Generated by Django 3.1.1 on 2020-09-03 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imgfile',
            new_name='image_file',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='img_url',
            new_name='image_url',
        ),
    ]