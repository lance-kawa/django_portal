# Generated by Django 4.2.9 on 2024-01-13 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0025_alter_projectimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='bg_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/cv_pictures/'),
        ),
    ]
