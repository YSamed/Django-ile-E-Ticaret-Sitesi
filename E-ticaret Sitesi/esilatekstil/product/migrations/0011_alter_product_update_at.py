# Generated by Django 4.2.10 on 2024-02-21 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_rename_images_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
