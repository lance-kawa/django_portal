# Generated by Django 4.2.9 on 2024-01-12 12:19

import os 
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0020_theme_category_order'),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
        DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
        DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')

        superuser = User.objects.create_superuser(
            username=DJANGO_SU_NAME,
            email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD)

        superuser.save()


    operations = [
        migrations.RunPython(generate_superuser),
    ]
