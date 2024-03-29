# Generated by Django 4.2.10 on 2024-02-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0007_settings_contact_settings_create_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='settings',
            old_name='instgaram',
            new_name='instagram',
        ),
        migrations.RenameField(
            model_name='settings',
            old_name='smptpport',
            new_name='smptport',
        ),
        migrations.RenameField(
            model_name='settings',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='settings',
            name='smptemail',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='settings',
            name='status',
            field=models.BooleanField(choices=[(True, 'Evet'), (False, 'Hayır')]),
        ),
    ]
