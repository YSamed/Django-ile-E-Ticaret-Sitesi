# Generated by Django 4.2.10 on 2024-02-21 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_rename_images_images_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='images',
            new_name='image',
        ),
    ]
