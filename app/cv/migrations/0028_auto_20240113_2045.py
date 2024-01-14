# Generated by Django 4.2.9 on 2024-01-13 20:45

from django.db import migrations


def load_data(apps, schema_editor):
    from django.core.management import call_command
    call_command('loaddata', 'cv/fixtures/manon_profil.json')

class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0027_load_data'),
    ]

    operations = [
        # migrations.RunPython(load_data),
    ]
