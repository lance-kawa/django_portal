# Generated by Django 4.2.9 on 2024-01-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0030_profil_job_profil_job_en_profil_job_fr'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='skill_display',
            field=models.TextField(blank=True, default=''),
        ),
    ]
