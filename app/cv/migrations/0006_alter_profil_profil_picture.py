# Generated by Django 4.2.7 on 2023-12-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_alter_profil_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='profil_picture',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/static/profil_pictures/'),
        ),
    ]
