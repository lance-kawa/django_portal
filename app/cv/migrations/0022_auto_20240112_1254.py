# Generated by Django 4.2.9 on 2024-01-12 12:54

from django.db import migrations

def load_data(apps, schema_editor):
    from django.core.management import call_command
    call_command('loaddata', 'cv/fixtures/kawa_profil.json')

class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0021_auto_20240112_1219'),
    ]

    operations = [
    ]