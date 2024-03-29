# Generated by Django 4.2.10 on 2024-02-22 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_category_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='status',
        ),
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AddField(
            model_name='category',
            name='gender',
            field=models.CharField(blank=True, choices=[('erkek', 'Erkek'), ('kadın', 'Kadın'), ('çocuk', 'Çocuk')], max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(blank=True, choices=[('erkek', 'Erkek'), ('kadın', 'Kadın'), ('çocuk', 'Çocuk')], max_length=10),
        ),
    ]
